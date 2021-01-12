from api import db


class Product(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    asin = db.Column(db.String(50), unique=True)
    title = db.Column(db.String(500), unique=False)
    # one Product by 'id' -> many Reviews
    review = db.relationship('Review', backref='product', lazy='dynamic')

    def __repr__(self):
        return '<Product {id} - {asin}>'.format(id=self.id, asin=self.asin)

    def get_data_by_id(self, id: str):
        # (?!) get by 'id' and join with 'Review' by 'asin'
        item_data = self.query.filter_by(id=id).first()
        return _data_to_dict(item_data)
    
    def _data_to_dict(self, item_data: Products):
        return {
            "id": item_data.id,
            "product_data": {
                "asin": item_data.asin,
                "title": item_data.title,
                "review": "Product review...",
            }
            "page_number": 1,
        }

    def save_to_db(self, data: dict):
        self.asin = data.get("asin")
        self.title = data.get("title")
        self.review = data.get("review")
        try:
            db.session.add(self)
            db.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()


class Review(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    asin = db.Column(db.String(50), unique=True)
    title = db.Column(db.String(500), unique=False)
    review = db.Column(db.Text, unique=False)

    product_asin = db.Column(db.String, db.ForeignKey('product.asin'))
