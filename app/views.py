from app import app, db
from app.models import Product, Review
from flask import request
from flask.json import jsonify


@app.route("/<product_id>", methods=["GET"])
def get(product_id):
    product = db.session.query(Product).get_or_404(product_id)
    reviews = []
    for rev in product.reviews:
        reviews.append({"review_title": rev.title, "review_text": rev.review_text})

    return jsonify({"id": product.id, "asin": product.asin, "reviews": reviews})


@app.route("/<product_id>", methods=["PUT"])
def put(product_id):
    product = db.session.query(Product).get_or_404(product_id)
    body = request.get_json()

    review = (
        db.session.query(Review)
        .filter_by(
            product_asin=product.asin,
            title=body.get("review_title"),
            review_text=body.get("review_text"),
        )
        .first()
    )
    if not review:
        review = Review(
            product_asin=product.asin,
            title=body.get("review_title"),
            review_text=body.get("review_text"),
        )
        db.session.add(review)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Exception: {e}")

    return jsonify(
        {
            "product_asin": review.product_asin,
            "title": review.title,
            "review_text": review.review_text,
        }
    )
