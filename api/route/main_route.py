from flask import Blueprint, Flask

from api.config.containers import APPContainer
from api.route.v1.v1_routes import register_v1_routes


def register_routes(app: Flask, container: APPContainer):
    v1 = Blueprint("v1", "v1", url_prefix="/api/v1")

    register_v1_routes(app, v1, container)

    app.register_blueprint(v1)
