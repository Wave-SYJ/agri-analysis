from . import db
from . import gen_id


class Province(db.Model):
    id = db.Column(db.String(32), default=gen_id, primary_key=True)
    name = db.Column(db.String(32), nullable=False)

    cities = db.relationship("City", backref="province", lazy="dynamic")

    def __init__(self):
        pass

    def __int__(self, name):
        self.name = name
