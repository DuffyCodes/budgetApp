from flask import Blueprint, jsonify
bp = Blueprint('alert', __name__)

@bp.route('/api/alert/send', methods=['POST'])
def send_alert():
    return jsonify({"message": "Alert send endpoint"})