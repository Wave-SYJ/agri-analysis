from . import db
from . import gen_id


class Market(db.Model):
    id = db.Column(db.String(32), default=gen_id, primary_key=True)
    city_id = db.Column(db.String(32), db.ForeignKey('city.id'), nullable=True)
    name = db.Column(db.String(32), nullable=False)
    details = db.Column(db.Text, nullable=True)

    def __init__(self):
        pass

    def __int__(self, name, details, city_id):
        self.name = name
        self.details = details
        self.city_id = city_id
