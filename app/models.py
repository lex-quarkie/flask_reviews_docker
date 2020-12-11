from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column, ForeignKey, Integer, String, Text
)


from app.app import db, app

Base = declarative_base()


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    asin = Column(String(255), nullable=False)
    reviews = relationship('Review', backref='product', lazy=True)

    def __repr__(self):
        return '<Product ASIN #{self.asin}>'

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True)
    product_asin = Column(String(255), nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False )
    title = Column(Text, nullable=False)
    review_text = Column(Text, nullable=False)

    def __repr__(self):
        return '<Review on ASIN #{self.product_asin}>'
