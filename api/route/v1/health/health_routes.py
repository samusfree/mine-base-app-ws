import logging
import traceback

from flask import Blueprint, jsonify
from sqlalchemy import text

from api.config.extensions import db

health_blueprint_v1 = Blueprint("health_bp", __name__)

logger = logging.getLogger(__name__)


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
                                db_status:
                                    type: boolean
                            example:
                                status : UP
        tags:
            - health
    """
    is_database_working = True

    try:
        db.session.execute(text("SELECT 1"))
    except Exception as e:
        logger.error("%s\n%s", e, traceback.format_exc(), exc_info=True)
        is_database_working = False

    return jsonify({"status": "UP", "db_status": is_database_working}), 200
