from api import db


class Product(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    asin = db.Column(db.String(50), unique=True)
    title = db.Column(db.String(500), unique=False)
    # one Product by 'id' -> many Reviews
    reviews = db.relationship('Review', backref='product')

    def __repr__(self):
        return '<Product: {id} - {asin}>'.format(id=self.id, asin=self.asin)

    def get_product(self, id: int) -> dict:
        product = self.find_product_by_id(id)
        if not product:
            return {'message': f'Product with id={id} not found!'}
        return self.prepare_json_response(product)

    def find_product_by_id(self, id: int):
        return self.query.filter_by(id=id).first()

    def prepare_json_response(self, product) -> dict:
        return {
            "id": product.id,
            "product_info": {
                "asin": product.asin,
                "title": product.title,
                "reviews": self.listing_reviews(product),
            },
        }

    def listing_reviews(self, product: list) -> list:
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

    def save_product(self, product: dict):
        self.asin = product.get("Asin")
        self.title = product.get("Title")
        self._save_to_db()

    def _save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
            print(f"Saved: {self}")
        except Exception as exc:
            db.session.rollback()
            print(f"Rollback: {exc}")
        finally:
            db.session.close()


class Review(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    asin = db.Column(db.String(50), unique=False)
    title = db.Column(db.String(500), unique=False)
    review = db.Column(db.Text, unique=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))

    def __repr__(self):
        return '<Review: {id} - {asin}>'.format(id=self.id, asin=self.asin)

    @staticmethod
    def update_review(review: dict, product_id: int):
        product = Review.query.filter_by(product_id=product_id).first()
        new_review = review.get("review")
        if product and review:
            product.review = new_review
        try:
            db.session.add(product)
            db.session.commit()
            print(f"Saved: {product}")
        except Exception as exc:
            db.session.rollback()
            print(f"Rollback: {exc}")
        finally:
            db.session.close()

    def save_to_db(self, data: dict):
        self.asin = data.get("Asin")
        self.title = data.get("Title")
        self.review = data.get("Review")

        product = Product.query.filter_by(asin=self.asin).first()
        self.product_id = product.id

        try:
            db.session.add(self)
            db.session.commit()
            print(f"Saved: {self}")
        except Exception as exc:
            db.session.rollback()
            print(f"Rollback: {exc}")
        finally:
            print("Session closed")
            db.session.close()
