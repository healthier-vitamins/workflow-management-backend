from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app_inner = Flask(__name__)
# CORS error, default settings
CORS(app_inner)
# config urls, secret key, etc
app_inner.config.from_object(Config)
# for login init
login = LoginManager(app_inner)
# sqlalchemy
db = SQLAlchemy(app_inner)
# migration 
migrate = Migrate(app_inner, db)

from app import routes, models
