import os
import csv
from functools import wraps

from api.models import Product, Review


datasets = [os.path.abspath(f"datasets/{csv}") for csv in os.listdir('datasets')]

# products_dataset = ""
# reviews_dataset = ""


# def parse_csv(func, filename: str):
#     @wraps
#     with open(filename) as data:
#         for item_data in csv.DictReader(data):
#             func(item_data)
#
#
def parse_products_csv(filename: str):
    with open(filename) as data:
        for item_data in csv.DictReader(data):
            print(item_data)
            product = Product()
            product.save_to_db(item_data)


def parse_reviews_csv(filename: str):
    with open(filename) as data:
        for item_data in csv.DictReader(data):
            print(item_data)
            review = Review()
            review.save_to_db(item_data)


if __name__ == "__main__":
    # products = datasets[0]
    # parse_products_csv(products)

    reviews = datasets[1]
    parse_reviews_csv(reviews)


