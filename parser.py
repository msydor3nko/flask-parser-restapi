import os
import csv

from api.models import Product, Review


class Parser(object):
    def __init__(self, csv_file_name: str, is_products_data: bool = True):
        self.csv_file = csv_file_name
        self.is_products = is_products_data

    def run(self):
        data_items = self.csv_rows_to_dicts(self.csv_file)
        for item in data_items:
            if self.is_products:
                self.save_products_into_db(item)
            else:
                self.save_reviews_into_db(item)

    def csv_rows_to_dicts(self, csv_file: str):
        with open(csv_file) as data:
            for row_data in csv.DictReader(data):
                yield row_data

    def save_products_into_db(self, item: dict):
        product = Product()
        product.save_parsed_product_to_db(item)

    def save_reviews_into_db(self, item: dict):
        review = Review()
        review.save_parsed_review_to_db(item)


if __name__ == "__main__":
    products_csv = os.path.join(os.path.abspath("datasets"), "products.csv")
    reviews_csv = os.path.join(os.path.abspath("datasets"), "reviews.csv")

    products_parser = Parser(csv_file_name=products_csv, is_products_data=True)
    reviews_parser = Parser(csv_file_name=reviews_csv, is_products_data=False)

    products_parser.run()
    reviews_parser.run()

