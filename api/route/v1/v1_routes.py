from flask import Blueprint, Flask

from api.config.containers import APPContainer

from .users import user_routes


def register_v1_routes(app: Flask, v1: Blueprint, container: APPContainer):
    v1.register_blueprint(user_routes.user_blueprint_v1)

    container.wire(modules=[user_routes])
