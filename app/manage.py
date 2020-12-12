
from input_csv import read_products

import click
from flask.cli import with_appcontext


@click.command(name='parse_csv')
@with_appcontext
def parse_csv():
    "Parsing csv files from input_csv/ folder"

    read_products()
