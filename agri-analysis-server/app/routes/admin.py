import json

from flask import Blueprint, jsonify, request, abort
from sqlalchemy import text
from werkzeug.security import generate_password_hash

from app.models import db
from app.models.admin import Admin
from app.utils.serialize import serialize

bp = Blueprint('admin_bp', __name__, url_prefix='/')


def list_admins():
    data = json.loads(request.get_data())

    query = Admin.query
    print(data)

    # search
    search_obj = data.get('searchObj', None)
    if search_obj is not None:
        if search_obj.get('username', None) is not None:
            query = query.filter(Admin.username == search_obj['username'])

    # sort
    sort_info = data.get('sortInfo', None)
    if sort_info is not None:
        if sort_info['order'] == 'ascending':
            query = query.order_by(text(sort_info['column']))
        else:
            query = query.order_by(text("-" + sort_info['column']))

    # pagination
    page_info = data.get('pagination', {
        'pageNo': 1,
        'pageSize': 10
    })
    page_no = page_info['pageNo']
    page_size = page_info['pageSize']
    query = query.paginate(page_no, per_page=page_size, error_out=False)

    items = serialize(query.items)
    for item in items:
        del item['password']

    items = serialize(query.items)
    return jsonify({
        "pageCount": query.pages,
        "pageNo": query.page,
        "pageSize": query.per_page,
        "total": query.total,
        "list": items
    })


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


@bp.route('/admin', methods=['PATCH', 'PUT', 'DELETE', 'POST'])
def index():
    if request.method == 'POST':
        return list_admins()
    elif request.method == 'PUT':
        return insert_admin()
    elif request.method == 'DELETE':
        return delete_admins()
    elif request.method == 'PATCH':
        return modify_admin()
    else:
        abort(404)
