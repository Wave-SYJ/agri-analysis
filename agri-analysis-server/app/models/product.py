from . import db
from . import gen_id


class Product(db.Model):
    id = db.Column(db.String(32), default=gen_id, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    variety_id = db.Column(db.String(32), db.ForeignKey("variety.id"), nullable=True)
    market_id = db.Column(db.String(32), db.ForeignKey("market.id"), nullable=True)
    price = db.Column(db.Float, nullable=True)
    date = db.Column(db.Date, nullable=True)

    def __init__(self):
        pass

    def __int__(self, name, type_id):
        self.name = name
        self.type_id = type_id
