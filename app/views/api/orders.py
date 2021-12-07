import json
import traceback

from flask import Blueprint, request, jsonify, Response
from flask_login import login_required

from app.core.controllers import order_controller

orders = Blueprint('orders_api', __name__)


@orders.route('/get_orders', methods=['POST'])
@login_required
def get_orders_view():
    d = json.loads(request.data)
    limit = int(d.get('limit', 0))
    offset = int(d.get('offset', 0))
    orders = order_controller.get_all_orders(limit=limit, offset=offset)
    return jsonify(orders)


@orders.route('/get_order', methods=['POST'])
@login_required
def get_order_view():
    order_id = json.loads(request.form.get('data'))
    order = order_controller.get_order(order_id)
    return jsonify(order)


@orders.route('/<string:order_id>/set_upd', methods=['POST'])
@login_required
def set_upd_view(order_id):
    upd = json.loads(request.form.get('data'))
    order = order_controller.set_upd(order_id, upd)
    return jsonify(order)


@orders.route('/<string:order_id>/download_upd', methods=['POST'])
@login_required
def download_upd_view(order_id):
    return order_controller.get_upd(order_id)


@orders.route('/<string:order_id>/download_bill', methods=['POST'])
@login_required
def download_bill_view(order_id):
    return order_controller.get_bill(order_id)


@orders.route('/<string:order_id>/close', methods=['POST'])
@login_required
def close_order_view(order_id):
    try:
        order = order_controller.close_order(order_id)
    except Exception as e:
        traceback.print_exc()
        return Response(str(e), status=409)
    return jsonify(order)


@orders.route('/<string:order_id>/checkout', methods=['POST'])
@login_required
def checkout_order_view(order_id):
    try:
        order = order_controller.checkout_order(order_id)
    except Exception as e:
        traceback.print_exc()
        return Response(str(e), status=409)
    return jsonify(order)
