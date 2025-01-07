from flask import Blueprint, jsonify
bp = Blueprint('budget', __name__)

@bp.route('/api/budget/total', methods=['GET'])
def total_budget():
    return jsonify({"message": "Total budget endpoint"})