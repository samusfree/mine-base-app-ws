from flask import jsonify
from marshmallow import ValidationError

from api.exception.not_found_error import NotFoundError


def handle_validation_error(err):
    response = jsonify(err.messages)
    response.status_code = 400
    return response


def handle_not_found_error(err):
    response = jsonify({"error": err.message})
    response.status_code = 404
    return response


def handle_generic_error(err):
    response = jsonify({"error": "An unexpected error occurred"})
    response.status_code = 500
    return response


def register_error_handlers(app):
    app.register_error_handler(ValidationError, handle_validation_error)
    app.register_error_handler(NotFoundError, handle_not_found_error)
    app.register_error_handler(Exception, handle_generic_error)
