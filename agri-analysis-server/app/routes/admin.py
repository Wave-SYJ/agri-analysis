import json

from flask import Blueprint, jsonify, request, abort
from werkzeug.security import generate_password_hash

from app.models import db
from app.models.admin import Admin
from app.utils.serialize import serialize

bp = Blueprint('admin_bp', __name__, url_prefix='/admin')


def list_admins():
    data = serialize(Admin.query.all())
    for item in data:
        del item['password']
    return jsonify(data)


def insert_admin():
    data = json.loads(request.get_data())
    data["password"] = generate_password_hash(data["username"])
    db.session.add(Admin(**data))
    db.session.commit()
    return ""


def delete_admins():
    data = json.loads(request.get_data())
    Admin.query.filter(Admin.id.in_(data)).delete()
    db.session.commit()
    return ""


def modify_admin():
    data = json.loads(request.get_data())
    Admin.query.filter_by(id=data["id"]).update(data)
    db.session.commit()
    return ""


@bp.route('/', methods=['GET', 'PUT', 'DELETE', 'POST'])
def index():
    if request.method == 'GET':
        return list_admins()
    elif request.method == 'PUT':
        return insert_admin()
    elif request.method == 'DELETE':
        return delete_admins()
    elif request.method == 'POST':
        return modify_admin()
    else:
        abort(404)
