import os
import csv


files_path = [os.path.abspath(x) for x in os.listdir('datasets')]


def parse_csv(file_path: str):
    with open(file_path) as csvfile:
        reader = csv.reader(csvfile)
        for row in spamreader:
            print(', '.join(row))


if __name__ == "__main__":
    parse_csv(files_path[0])