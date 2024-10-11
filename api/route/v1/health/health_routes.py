from flask import Blueprint, jsonify

health_blueprint_v1 = Blueprint("health_bp", __name__)


@health_blueprint_v1.route("/health-check", methods=["GET"])
def health():
    """
    Health check endpoint
    ---
    get:
        description: Health check endpoint
        responses:
            200:
                description: Health check response
                content:
                    application/json:
                        schema:
                            type: object
                            properties:
                                status:
                                    type: string
                            example: 
                                status : UP
        tags:
            - health
        """
    return jsonify({"status": "UP"}), 200
