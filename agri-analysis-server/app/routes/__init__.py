from .admin import bp as admin_bp


def init_app(app):
    app.register_blueprint(admin_bp)
