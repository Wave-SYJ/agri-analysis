import json

from flask import Blueprint, request

bp = Blueprint('predict_bp', __name__)


@bp.route('/predict', methods=['POST'])
def get_predict_data():
    data = json.loads(request.get_data())
    print(data)
    return '2323'
