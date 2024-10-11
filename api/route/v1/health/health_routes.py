from flask import Blueprint, jsonify

health_blueprint_v1 = Blueprint("health_bp", __name__)


@health_blueprint_v1.route("/health-check", methods=["GET"])
def health():
    return jsonify({"status": "UP"}), 200
