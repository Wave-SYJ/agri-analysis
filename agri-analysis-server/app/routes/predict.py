import json

from flask import Blueprint, request
from app.spark import df_reader
import pyspark.sql.functions as f
from functools import reduce

bp = Blueprint('predict_bp', __name__)


@bp.route('/predict', methods=['POST'])
def get_predict_data():
    data = json.loads(request.get_data())

    t_product = df_reader('t_product').alias('t_product')
    count_df = t_product.filter((t_product.date >= data['dateRange'][0]) & (t_product.date <= data['dateRange'][1]) &
                                (t_product.market_id == data['marketId']) & (t_product.variety_id == data['varietyId']))

    count_df.show()

    return '2323'
