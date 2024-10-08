from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from apispec_ui.flask import Swagger


def configureSwagger(app):
    spec = APISpec(
        title="Base API",
        version="1.0.0",
        openapi_version="3.0.2",
        plugins=[FlaskPlugin(), MarshmallowPlugin()],
    )

    # Register the path and the entities within it
    with app.test_request_context():
        for rule in app.url_map.iter_rules():
            if rule.endpoint != "static":
                view_func = app.view_functions[rule.endpoint]
                spec.path(view=view_func)
                

    Swagger(app=app, apispec=spec, config={})
