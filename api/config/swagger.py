import json

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from swagger_ui import api_doc

from api.schema.user_schema import UserSchema


def configure_swagger(app):
    apispec = APISpec(
        title="Base API",
        version="1.0.0",
        openapi_version="3.0.2",
        plugins=[FlaskPlugin(), MarshmallowPlugin()],
        info={
            "description": "Base API with Flask, dependency injector, "
            + "SQLAlchemy, Marshmallow, and Flask-Migrate"
        },
    )

    apispec.tag({"name": "users", "description": "Operations related to users"})
    apispec.components.schema("UserSchema", schema=UserSchema)

    with app.test_request_context():
        for rule in app.url_map.iter_rules():
            if rule.endpoint != "static":
                view_func = app.view_functions[rule.endpoint]
                apispec.path(view=view_func)

    api_doc(
        app,
        config_spec=json.dumps(apispec.to_dict(), indent=2),
        url_prefix="/api/doc",
        title="Base API",
    )
