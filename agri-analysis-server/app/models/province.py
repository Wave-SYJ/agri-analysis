from . import db
from . import gen_id


class Province(db.Model):
    id = db.Column(db.String(32), default=gen_id, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
