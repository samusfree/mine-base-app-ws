import pytest
from flask import Flask
from flask.testing import FlaskClient

from api import APPInitializer


@pytest.fixture
def app():
    app_unit = APPInitializer("unittest").init_app()
    return app_unit


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()
