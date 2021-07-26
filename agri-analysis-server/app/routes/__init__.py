from .admin import bp as admin_bp
from .category import bp as category_bp
from .monitor import bp as monitor_bp
from .product import bp as product_bp
from .region import bp as region_bp


def init_app(app):
    app.register_blueprint(admin_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(monitor_bp)
    app.register_blueprint(region_bp)
