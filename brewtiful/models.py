
from . import db
from datetime import datetime

orderdetails = db.Table('order_details',
    db.Column('order_id', db.Integer, db.ForeignKey('orders.id'), nullable=False),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), nullable=False),
    db.Column('quantity', db.Integer, nullable=False, default=1),
    db.PrimaryKeyConstraint('order_id', 'product_id'))

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Float, nullable=False)
    size = db.Column(db.String(64), nullable=False)
    origin = db.Column(db.String(64), nullable=False)
    is_blend = db.Column(db.Boolean, nullable=False)
    aroma = db.Column(db.String(500), nullable=False)
    notes = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return f"Product(id={self.id}, name={self.name}, price={self.price}, is_blend={self.is_blend})"

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    firstname = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    street = db.Column(db.String(128))
    suburb = db.Column(db.String(64))
    postcode = db.Column(db.String(32))
    country = db.Column(db.String(64))
    email = db.Column(db.String(128))
    phone = db.Column(db.String(32))
    total_cost = db.Column(db.Float)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    products = db.relationship("Product", secondary=orderdetails, backref="orders")

    def __repr__(self):
        return f"Order(id={self.id}, status={self.status}, total_cost={self.total_cost})"