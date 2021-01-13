import os
import csv

from api.models import Product, Review


products_csv = os.path.join(os.path.abspath("datasets"), "products.csv")
reviews_csv = os.path.join(os.path.abspath("datasets"), "reviews.csv")


def parse_and_save_products(filename: str):
    with open(filename) as data:
        for item_data in csv.DictReader(data):
            product = Product()
            product.save_product(item_data)


def parse_and_save_reviews(filename: str):
    with open(filename) as data:
        for item_data in csv.DictReader(data):
            review = Review()
            review.save_to_db(item_data)


if __name__ == "__main__":
    parse_and_save_products(products_csv)
    parse_and_save_reviews(reviews_csv)