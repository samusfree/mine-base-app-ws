import logging
import traceback

from flask import jsonify
from marshmallow import ValidationError

from api.exception.not_found_error import NotFoundError

logger = logging.getLogger(__name__)


def handle_validation_error(err):
    logger.error(err.messages, exc_info=True)
    response = jsonify(err.messages)
    response.status_code = 400
    return response


def handle_not_found_error(err):
    logger.error(err.message, exc_info=True)
    response = jsonify({"error": err.message})
    response.status_code = 404
    return response


def handle_generic_error(err: Exception):
    logger.error(f"{err}\n{traceback.format_exc()}", exc_info=True)
    # print(traceback.format_exc())

    response = jsonify({"error": "An unexpected error occurred"})
    response.status_code = 500
    return response


def handle_404_error(err):
    logger.error(f"{err}\n{traceback.format_exc()}", exc_info=True)
    response = jsonify({"error": "Page not found"})
    response.status_code = 404
    return response


def register_error_handlers(app):
    app.register_error_handler(ValidationError, handle_validation_error)
    app.register_error_handler(NotFoundError, handle_not_found_error)
    app.register_error_handler(404, handle_404_error)
    app.register_error_handler(Exception, handle_generic_error)
