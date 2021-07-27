from sqlalchemy.orm import backref

from . import db
from . import gen_id
from .market import Market
from .variety import Variety
from sqlalchemy_serializer import SerializerMixin


class Product(db.Model, SerializerMixin):
    __tablename__ = 't_product'

    id = db.Column(db.String(32), default=gen_id, primary_key=True)
    variety_id = db.Column(db.String(32), db.ForeignKey(Variety.id), nullable=True)
    market_id = db.Column(db.String(32), db.ForeignKey(Market.id), nullable=True)
    price = db.Column(db.Float, nullable=True)
    date = db.Column(db.Date, nullable=True)
    sell_number = db.Column(db.Integer, nullable=True)

    market = db.relationship("Market")
    variety = db.relationship("Variety")

    def __init__(self):
        pass

    def __int__(self, name, price, date):
        self.name = name
        self.price = price
        self.date = date
