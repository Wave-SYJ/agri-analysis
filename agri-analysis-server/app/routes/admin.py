import json

from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash

from app.models import db
from app.models.admin import Admin
from app.utils.serialize import serialize

bp = Blueprint('admin_bp', __name__, url_prefix='/admin')


def list_admin():
    return jsonify(serialize(Admin.query.all()))


def insert_admin():
    data = json.loads(request.get_data())
    data["password"] = generate_password_hash(data["username"])
    db.session.add(Admin(**data))
    db.session.commit()
    return ""


@bp.route('/', methods=['GET', 'PUT'])
def index():
    if request.method == 'GET':
        return list_admin()
    elif request.method == 'PUT':
        return insert_admin()
