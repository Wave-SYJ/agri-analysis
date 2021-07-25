import json

from flask import Blueprint, jsonify
from app.models.market import Market
from app.models.type import Type
from app.models.variety import Variety
from app.models.product import Product

bp = Blueprint('monitor_bp', __name__, url_prefix='/monitor')


@bp.route('/basic', methods=['GET', 'PUT', 'DELETE', 'POST'])
def basic_info():
    return jsonify({
        'marketTotal': Market.query.count(),
        'typeTotal': Type.query.count(),
        'varietyTotal': Variety.query.count(),
        'productTotal': Product.query.count()
    })
