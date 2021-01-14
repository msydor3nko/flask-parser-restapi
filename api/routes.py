from flask import request

from api import app, cache
from api.models import Product, Review


@app.route('/api/products/<int:id>', methods=["GET"])
@cache.cached(timeout=10)
def get_product_info(id):
    product = Product()
    product_info = product.get_product_from_db(id=id)
    return product_info, 200


@app.route('/api/reviews/<int:id>', methods=["PUT"])
def add_new_product_review(id):
    review = Review()
    review_status = review.add_new_product_review(new_review=request.json, product_id=id)
    return review_status
