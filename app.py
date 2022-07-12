from flask import Flask, jsonify, request, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = os.environ['SECRET_KEY']

db = SQLAlchemy(app)

@app.route("/")
def index():
    print(type(app))
    return "hello"
