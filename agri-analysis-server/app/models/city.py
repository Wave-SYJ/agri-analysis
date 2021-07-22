from . import db
from . import gen_id


class City(db.Model):
    id = db.Column(db.String(32), default=gen_id, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    province_id = db.Column(db.String(32), db.ForeignKey("province.id"), nullable=False)

    def __init__(self):
        pass

    def __int__(self, name, province_id):
        self.name = name
        self.province_id = province_id
