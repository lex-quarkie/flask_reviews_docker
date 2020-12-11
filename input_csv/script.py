import csv

REVIEWS_FILENAME = '../input_csv/reviews.csv'
PRODUCTS_FILENAME = '../input_csv/products.csv'
with open(REVIEWS_FILENAME, newline='') as csvfile:
    reviews = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for obj in reviews:
        from pudb import set_trace; set_trace()

        asin = obj.pop(0)
        print(row)
