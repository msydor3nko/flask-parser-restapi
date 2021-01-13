from flask import request, jsonify

from api import app, cache
from api.models import Product, Review


@app.route('/api/products/<int:id>', methods=["GET"])
@cache.cached(timeout=10)
def get_product(id):
    product = Product()
    return product.get_product(id=id), 200


@app.route('/api/reviews/<int:id>', methods=["PUT"])
def update_product_review(id):
    Review.update_review(review=request.json, product_id=id)
    return {"message": f"Updated review for product with id = {id}"}, 201