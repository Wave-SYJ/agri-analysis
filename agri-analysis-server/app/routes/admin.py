from flask import Blueprint, jsonify

from app.models.admin import Admin
from app.utils.serialize import serialize

bp = Blueprint('admin_bp', __name__, url_prefix='/admin')


@bp.route('/', methods=['GET'])
def index():
    return jsonify(serialize(Admin.query.all()))
