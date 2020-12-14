from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Text

Base = declarative_base()


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    title = Column(String(5000), nullable=False)
    asin = Column(String(500), nullable=False, unique=True)
    reviews = relationship("Review", backref="product", lazy=True)

    def __repr__(self):
        return f"<Product ASIN #{self.asin}>"


class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True)
    product_asin = Column(String(500), ForeignKey("products.asin"), nullable=False)
    title = Column(String(5000), nullable=False)
    review_text = Column(String(15000), nullable=False)

    def __repr__(self):
        return f"<Review #{self.id} on ASIN #{self.product_asin}>"
