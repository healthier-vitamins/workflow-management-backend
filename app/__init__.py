from flask import Flask
from flask_cors import CORS
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app_inner = Flask(__name__)
app_inner.config.from_object(Config)
db = SQLAlchemy(app_inner)
migrate = Migrate(app_inner, db)

from app import routes, models
