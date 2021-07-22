from flask import Blueprint
from app.models.admin import Admin
from app.models import db

bp = Blueprint('admin_bp', __name__, url_prefix='/admin')


@bp.route('/', methods=['GET'])
def index():
    user = Admin("super", "root")
    db.session.add(user)
    db.session.commit()

    return str(Admin.query.all())
