import os
from flask_cors import CORS


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
        cls.SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(app.root_path, '../db/data.sqlite')
        CORS(app, supports_credentials=True)


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
