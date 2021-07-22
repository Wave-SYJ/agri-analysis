from . import db
from . import gen_id


class Type(db.Model):
    id = db.Column(db.String(32), default=gen_id, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    type_id = db.Column(db.String(32), db.ForeignKey("type.id"), nullable=False)

    products = db.relationship("Product", backref="varieties", lazy="dynamic")

    def __init__(self):
        pass

    def __int__(self, name, type_id):
        self.name = name
        self.type_id = type_id
