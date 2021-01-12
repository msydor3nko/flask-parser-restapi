from api import db


class Product(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    asin = db.Column(db.String(50), unique=True)
    title = db.Column(db.String(500), unique=False)
    # one Product by 'id' -> many Reviews
    review = db.relationship('Review', backref='product', lazy='dynamic')

    def __repr__(self):
        return '<Product {id} - {asin}>'.format(id=self.id, asin=self.asin)

    @staticmethod
    def get_data_by_id(product_id: int):
        # (?!) get by 'id' and join with 'Review' by 'asin'
        item_data = Product.query.filter_by(id=product_id).first()
        return Product._data_to_dict(item_data)

    @classmethod
    def _data_to_dict(cls, item_data):
        return {
            "id": item_data.id,
            "product_data": {
                "asin": item_data.asin,
                "title": item_data.title,
                "review": "Product review...",
            },
            "page_number": 1,
        }

    def save_to_db(self, data: dict):
        self.asin = data.get("Asin")
        self.title = data.get("Title")

        try:
            db.session.add(self)
            db.session.commit()
            print(f"Saved: {self.asin}")
        except Exception as exc:
            print(f"Rollback: {exc}")
            db.session.rollback()
        finally:
            print("Session closed")
            db.session.close()


class Review(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    asin = db.Column(db.String(50), unique=True)
    title = db.Column(db.String(500), unique=False)
    review = db.Column(db.Text, unique=False)

    # (?!) asin should be
    product_id = db.Column(db.String, db.ForeignKey('product.id'))

    @staticmethod
    def update_review(review: dict, product_id: int):
        product = Product.query.filter_by(id=id).first()
        if product:
            product.review = review.get("review")
        try:
            db.session.add(product)
            db.session.commit()
            print(f"Saved: {product.asin}")
        except Exception as exc:
            db.session.rollback()
            print(f"Rollback: {exc}")
        finally:
            print("Session closed")
            db.session.close()

    def save_to_db(self, data: dict):
        self.asin = data.get("Asin")
        self.title = data.get("Title")
        self.review = data.get("Review")

        product = Product.query.filter_by(asin=self.asin).first()
        print("product", product)
        self.product_id = product.id

        try:
            db.session.add(self)
            db.session.commit()
            print(f"Saved: {self.asin}")
        except Exception as exc:
            db.session.rollback()
            print(f"Rollback: {exc}")
        finally:
            print("Session closed")
            db.session.close()
