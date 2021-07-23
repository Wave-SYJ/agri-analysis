import json

from flask import Blueprint, jsonify, request, abort
from werkzeug.security import generate_password_hash

from app.models import db
from app.models.product import Product
from app.utils.serialize import serialize

bp = Blueprint('product_bp', __name__, url_prefix='/product')


def list_products():
    page_no = request.args.get('pageNo', 1, type=int)
    page_size = request.args.get('pageSize', 10, type=int)
    pagination = Product.query.paginate(page_no, per_page=page_size, error_out=False)
    items = serialize(pagination.items)
    return jsonify({
        "pageCount": pagination.pages,
        "pageNo": pagination.page,
        "pageSize": pagination.per_page,
        "total": pagination.total,
        "list": items
    })


def insert_product():
    data = json.loads(request.get_data())
    db.session.add(Product(**data))
    db.session.commit()
    return ""


def delete_products():
    data = json.loads(request.get_data())
    Product.query.filter(Product.id.in_(data)).delete()
    db.session.commit()
    return ""


def modify_product():
    data = json.loads(request.get_data())
    Product.query.filter_by(id=data["id"]).update(data)
    db.session.commit()
    return ""


@bp.route('/', methods=['GET', 'PUT', 'DELETE', 'POST'])
def index():
    if request.method == 'GET':
        return list_products()
    elif request.method == 'PUT':
        return insert_product()
    elif request.method == 'DELETE':
        return delete_products()
    elif request.method == 'POST':
        return modify_product()
    else:
        abort(404)
