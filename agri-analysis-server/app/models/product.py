from . import db
from . import gen_id
from .variety import Variety
from .market import Market


class Product(db.Model):
    __tablename__ = 't_product'

    id = db.Column(db.String(32), default=gen_id, primary_key=True)
    variety_id = db.Column(db.String(32), db.ForeignKey(Variety.id), nullable=True)
    market_id = db.Column(db.String(32), db.ForeignKey(Market.id), nullable=True)
    price = db.Column(db.Float, nullable=True)
    date = db.Column(db.Date, nullable=True)

    def __init__(self):
        pass

    def __int__(self, name, price, date):
        self.name = name
        self.price = price
        self.date = date
