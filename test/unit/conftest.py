from flask import Flask
from flask.testing import FlaskClient
import pytest
from api import APPInitializer


@pytest.fixture
def app():
    app = APPInitializer("unittest").init_app()
    return app


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()
