from . import db
from . import gen_id


class Admin(db.Model):
    id = db.Column(db.String(32), default=gen_id, primary_key=True)
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __int__(self):
        pass

    def __init__(self, username, password):
        self.username = username
        self.password = password
