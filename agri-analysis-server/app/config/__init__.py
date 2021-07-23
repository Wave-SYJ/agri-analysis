import os
from flask_cors import CORS
from sqlalchemy.engine import URL
import yaml


class BaseConfig:  # 基本配置类
    SECRET_KEY = os.getenv('SECRET_KEY', 'some secret words')
    ITEMS_PER_PAGE = 10

    def __init__(self):
        self.app = None

    @classmethod
    def init_app(cls, app):
        cls.app = app


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @classmethod
    def init_app(cls, app):
        super().init_app(app)
        mysql_config = yaml.load(open('app/config/database.secret.yml'),
                                 Loader=yaml.SafeLoader)['development']['database']

        cls.SQLALCHEMY_DATABASE_URI = URL(drivername=mysql_config['drivername'], username=mysql_config['username'],
                                          password=mysql_config['password'],
                                          host=mysql_config['host'], port=mysql_config['port'],
                                          database=mysql_config['database'])
        CORS(app, supports_credentials=True)


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
