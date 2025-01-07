from flask import Blueprint, jsonify
bp = Blueprint('plaid', __name__)

@bp.route('/api/plaid/link', methods=['POST'])
def link():
    return jsonify({"message": "Plaid link endpoint"})