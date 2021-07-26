from datetime import date

from flask import Flask
from flask.json import JSONEncoder

from app.config import config
from . import models, routes


class MyJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, date):
            return o.isoformat()

        return super().default(o)


def create_app(config_name='default'):
    app = Flask(__name__)
    config[config_name].init_app(app)
    app.config.from_object(config[config_name])
    app.json_encoder = MyJSONEncoder

    models.init_app(app)
    routes.init_app(app)

    return app
