import os

import pytest
from flask_migrate import downgrade, upgrade
from testcontainers.postgres import PostgresContainer

from api import APPInitializer


@pytest.fixture(scope="module")
def test_client():
    postgres = PostgresContainer("postgres:16")
    postgres.start()

    os.environ["POSTGRES_URL"] = postgres.get_connection_url()

    app = APPInitializer("integration").init_app()
    app.config["TESTING"] = True
    client = app.test_client()

    # Apply migrations
    with app.app_context():
        upgrade("migrations")

    yield client

    # Downgrade migrations
    with app.app_context():
        downgrade("migrations", revision="base")

    postgres.stop()
