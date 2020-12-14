import click
from flask import Flask
from flask_caching import Cache
from flask.cli import with_appcontext
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.config import Config
from app.models import Product, Review
from input_csv import read_products, read_reviews


@click.command(name="parse_csv")
@with_appcontext
def parse_csv():
    "Parsing csv files from input_csv/ folder"
    products = read_products()  # product_title, asin
    reviews = read_reviews()  # asin, review_title, review_text

    for row in products:
        product = Product(title=row[0], asin=row[1])
        db.session.add(product)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Exception: {e}")

    for row in reviews:
        review = Review(product_asin=row[0], title=row[1], review_text=row[2])
        db.session.add(review)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Exception: {e}")


db = SQLAlchemy(session_options={"autoflush": False})
migrate = Migrate()

cache = Cache(config={"CACHE_TYPE": "simple",
                      "CACHE_DEFAULT_TIMEOUT": 300})


def init_app(config_class=Config):


    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    app.cli.add_command(parse_csv)
    cache.init_app(app)

    return app


app = init_app()


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Product": Product, "Review": Review}


from app.views import *
