import os
import csv

from api.models import Product, Review


products_csv = os.path.join(os.path.abspath("datasets"), "products.csv")
reviews_csv = os.path.join(os.path.abspath("datasets"), "reviews.csv")


class Parser(object):

    def __init__(self, csv_name: str):
        self.csv_file = csv_name

    def run(self):
        data_items = self.csv_rows_to_dicts(self.csv_file)
        for item in data_items:
            self.save_item_to_db(item)

    def csv_rows_to_dicts(self, csv_file: str):
        with open(csv_file) as data:
            for data_item in csv.DictReader(data):
                yield data_item

    def save_item_to_db(self, data_item: dict):
        print(data_item)


def parse_and_save_products(filename: str):
    with open(filename) as data:
        for item_data in csv.DictReader(data):
            product = Product()
            product.save_parsed_product_to_db(item_data)


def parse_and_save_reviews(filename: str):
    with open(filename) as data:
        for item_data in csv.DictReader(data):
            review = Review()
            review.save_parsed_review_to_db(item_data)


if __name__ == "__main__":
    # parse_and_save_products(products_csv)
    parse_and_save_reviews(reviews_csv)

    # parser = Parser(products_csv)
    # parser.run()
