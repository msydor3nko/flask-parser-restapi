from flask import request

from api import app, cache
from api.models import Product, Review


@app.route('/api/products/<int:id>', methods=["GET"])
@cache.cached()
def get_product(id):
    return Product.get_data_by_id(product_id=id)


@app.route('/api/reviews/<int:id>', methods=["PUT"])
def send_review(id):
    return Product.update_review(review=request.json, product_id=id)
