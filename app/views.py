from app import app, db
from app.models import Product, Review
from flask.json import jsonify


@app.route("/<product_id>")
def hello(product_id):
    product = db.session.query(Product).get(product_id)

    return jsonify({"id": product.id,
                    "asin": product.asin,
                    "reviews": product.reviews})
