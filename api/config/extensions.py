from flask_migrate import Migrate
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

migrate = Migrate()
cors = CORS()
db = SQLAlchemy()
