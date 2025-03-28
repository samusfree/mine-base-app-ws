import os

from flask import Flask

from api.config.compress import compress_config
from api.config.config import Config
from api.config.containers import APPContainer
from api.config.extensions import cors, db, migrate
from api.config.logging_config import configure_logging
from api.config.swagger import configure_swagger
from api.route.main_route import register_routes
from api.util.error_handlers import register_error_handlers


class APPInitializer:
    def __init__(self, env=None):
        self.env = env

    def init_app(self):
        app = Flask(__name__)
        configure_logging(app)
        app.config.from_object(Config)

        container = APPContainer()
        container.config.config.from_dict(app.config)
        container.init_resources()

        if self.env == "unittest":
            app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        elif self.env == "integration":
            app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
                "POSTGRES_URL"
            )

        db.init_app(app)

        migrate.init_app(app, db)

        compress_config(app)

        cors.init_app(app)

        register_routes(app, container)

        app.container = container

        register_error_handlers(app)

        configure_swagger(app)

        return app
