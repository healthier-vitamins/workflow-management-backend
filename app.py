from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from models import User_Accounts, Job_Positions
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

# @app.route("/")

# engine = create_engine(os.environ['DATABASE_URL'], echo=True, future=True)

if __name__ == '__main__':
    # db.create_all(engine)
    app.run(debug=True)
