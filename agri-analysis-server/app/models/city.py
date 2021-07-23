from . import db
from . import gen_id
from .province import Province


class City(db.Model):
    __tablename__ = 't_city'

    id = db.Column(db.String(32), default=gen_id, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    province_id = db.Column(db.String(32), db.ForeignKey(Province.id), nullable=False)

    markets = db.relationship("Market", backref="city", lazy="dynamic")

    def __init__(self):
        pass

    def __int__(self, name, province_id):
        self.name = name
        self.province_id = province_id
