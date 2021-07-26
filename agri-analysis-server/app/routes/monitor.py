import json

from flask import Blueprint, jsonify, request

from app.models.market import Market
from app.models.product import Product
from app.models.type import Type
from app.models.variety import Variety
from app.spark import df_reader
from app.spark import spark

bp = Blueprint('monitor_bp', __name__, url_prefix='/monitor')


@bp.route('/basic', methods=['GET'])
def basic_info():
    return jsonify({
        'marketTotal': Market.query.count(),
        'typeTotal': Type.query.count(),
        'varietyTotal': Variety.query.count(),
        'productTotal': Product.query.count(),
    })


@bp.route('/crawls', methods=['POST'])
def get_crawls():
    data = json.loads(request.data)

    t_product = df_reader('t_product')
    t_variety = df_reader('t_variety')
    t_type = df_reader('t_type')

    count_df = t_product.filter(
        (t_product.date >= data['dateRange'][0]) & (t_product.date <= data['dateRange'][1])
        & (t_product.market_id == data['market'])) \
        .join(t_variety, t_product.variety_id == t_variety.id, 'left_outer') \
        .join(t_type, t_variety.type_id == t_type.id).groupby('date', "type_id").count()

    count_df = count_df.select("date", "type_id", "count")

    return jsonify(count_df.toJSON().collect())
