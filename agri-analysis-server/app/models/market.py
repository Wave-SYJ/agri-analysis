from . import db
from . import gen_id
from .city import City


class Market(db.Model):
    __tablename__ = 't_market'

    id = db.Column(db.String(32), default=gen_id, primary_key=True)
    city_id = db.Column(db.String(32), db.ForeignKey(City.id), nullable=True)
    name = db.Column(db.String(32), nullable=False)
    details = db.Column(db.Text, nullable=True)

    products = db.relationship("Product", backref="market", lazy="dynamic")

    def __init__(self):
        pass

    def __int__(self, name, details, city_id):
        self.name = name
        self.details = details
        self.city_id = city_id
