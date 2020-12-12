from csv import reader
import logging
import os


basedir = os.path.abspath(os.path.dirname(__file__))

PRODUCTS_FILENAME = os.path.join(basedir + '/products.csv')
REVIEWS_FILENAME = os.path.join(basedir + '/reviews.csv')

logging.basicConfig(level=logging.DEBUG)


def read_products():
    with open(PRODUCTS_FILENAME, 'r') as read_obj:
        csv_reader = reader(read_obj)
        logging.debug('Parsing started')
        header = next(csv_reader)
        # Check file as empty
        if header:
            parsed_rows = []
            for row in csv_reader:
                parsed_rows.append(row)

def read_reviews():
    with open(REVIEWS_FILENAME, 'r') as read_obj:
        csv_reader = reader(read_obj)
        logging.debug('Parsing started')
        header = next(csv_reader)
        # Check file as empty
        if header:
            parsed_rows = []
            for row in csv_reader:
                parsed_rows.append(row)

