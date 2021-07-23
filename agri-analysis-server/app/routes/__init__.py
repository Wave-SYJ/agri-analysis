from .admin import bp as admin_bp
from .product import bp as product_bp


def init_app(app):
    app.register_blueprint(admin_bp)
    app.register_blueprint(product_bp)
