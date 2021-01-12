from flask import request

from api import app


@app.route('/api/get_product/<int:id>', methods=["GET"])
# cache needed
def get_product():
    print("get_product")
    return {}


@app.route('/api/put_review', methods=["PUT"])
def send_review():
    print("Review putted")
    return {}
