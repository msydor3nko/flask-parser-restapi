from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError

from api import db
from api.response_messages import ResponseMessage
from api.exceptions import ProductNotFoundError, ReviewMissedDataError


class Product(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    asin = db.Column(db.String(50), unique=True)
    title = db.Column(db.String(500), unique=False)
    reviews = db.relationship('Review', backref='product')

    def __repr__(self):
        return '<Product: {id} - {asin}>'.format(id=self.id, asin=self.asin)

    def get_product_from_db(self, id: int):
        product = self.query.filter_by(id=id).first()
        if not product:
            return jsonify(ResponseMessage.PRODUCT_NOT_FOUND_400.value), 400
        response = self.prepare_json_response(product)
        return jsonify(response), 200

    def prepare_json_response(self, product) -> dict:
        return {
            "id": product.id,
            "product_info": {
                "asin": product.asin,
                "title": product.title,
                "reviews": self._listing_product_reviews(product),
            },
        }

    def _listing_product_reviews(self, product: list) -> list:
        reviews_list = []
        reviews = product.reviews
        if reviews:
            for item, review in enumerate(reviews, start=1):
                reviews_list.append(
                    {
                        "item": item,
                        "title": review.title,
                        "review": review.review,
                    }
                )
        return reviews_list

    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
            print(f"Saved: {self}")
        except SQLAlchemyError as exc:
            db.session.rollback()
            print(f"Rollback message: {exc}")
        finally:
            db.session.close()

    def save_parsed_product_to_db(self, product: dict):
        self.asin = product.get("Asin")
        self.title = product.get("Title")
        self.save_to_db()


class Review(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    asin = db.Column(db.String(50), unique=False)
    title = db.Column(db.String(500), unique=False)
    review = db.Column(db.Text, unique=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))

    def __repr__(self):
        return '<Review: {id} - {asin}>'.format(id=self.id, asin=self.asin)

    def add_new_product_review(self, new_review: dict, product_id: int):
        try:
            reviewed_product = self.find_review_by_product_id(product_id)
        except ProductNotFoundError:
            return jsonify(ResponseMessage.PRODUCT_NOT_FOUND_400.value), 400
        try:
            self.prepare_new_product_review_to_saving(new_review, reviewed_product)
        except ReviewMissedDataError:
            return jsonify(ResponseMessage.INCORRECT_REVIEW_FORMAT_400.value), 400
        self.save_to_db()
        return jsonify(ResponseMessage.NEW_REVIEW_CREATED_201.value), 201

    def find_review_by_product_id(self, product_id: int):
        reviewed_product = Review.query.filter_by(product_id=product_id).first()
        if not reviewed_product:
            raise ProductNotFoundError(reviewed_product)
        return reviewed_product

    def prepare_new_product_review_to_saving(self, new_review, reviewed_product):
        review_title = new_review.get("title")
        review_content = new_review.get("review")
        if not review_title or not review_content:
            raise ReviewMissedDataError(new_review)
        self.title = review_title
        self.review = review_content
        self.asin = reviewed_product.asin
        self.product_id = reviewed_product.product_id

    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
            print(f"Saved: {self}")
        except SQLAlchemyError as exc:
            db.session.rollback()
            print(f"Rollback message: {exc}")
        finally:
            db.session.close()

    def save_parsed_review_to_db(self, review_data):
        self.title = review_data.get("Title")
        self.review = review_data.get("Review")
        self.asin = review_data.get("Asin")
        if self.asin:
            product = Product.query.filter_by(asin=self.asin).first()
            self.product_id = product.id
        self.save_to_db()
