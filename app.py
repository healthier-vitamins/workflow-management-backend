from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import User_Accounts, Job_Positions
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = os.environ['SECRET_KEY']

db = SQLAlchemy(app)
# setup for migration
migrate = Migrate(app, db)

## flask db init
def create_app():
    db.init_app(app)
    migrate.init_app(app, db)
    return app

@app.route("/")
def index():
    print(type(app))
    return "hello"

@app.route("/create-new-user", methods=['POST'])
def addNewUser():
    return "sup"


# engine = create_engine(os.environ['DATABASE_URL'], echo=True, future=True)

if __name__ == '__main__':
    # db.create_all(engine)
    app.run(debug=True)
