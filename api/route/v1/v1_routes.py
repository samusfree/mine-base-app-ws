from flask import Blueprint

from api.config.containers import APPContainer
from api.route.v1.health import health_routes
from api.route.v1.users import user_routes


def register_v1_routes(v1: Blueprint, container: APPContainer):
    v1.register_blueprint(user_routes.user_blueprint_v1)
    v1.register_blueprint(health_routes.health_blueprint_v1)

    container.wire(modules=[user_routes])
