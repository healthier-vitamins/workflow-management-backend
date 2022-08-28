'''populating database without migrate, only sqlalchemy'''
#! from sqlalchemy import db.Boolean, Column, db.Integer, db.String, ForeignKey, create_engine
#! from sqlalchemy.orm import declarative_base, relationship

# if a database is initialised, Base shall hold it
#! Base = declarative_base()
''''''


from app import db
# hashing of password
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

'''flask-wtf sign'''
# allows methods/implementations for easier use
#! from flask_login import UserMixin
''''''

'''flask-wtf sigh'''
# to aid flask-login with navigating databases.
# login initialised in __init__.py.
# id passed through is string, therefore, casted.
#! @login.user_loader
#! def load_user(id):
#!     return User_Accounts.query.get(int(id))
''''''

'''flask-wtf sign'''
# UserMixin adds, User_Accounts.is_authenticated/.is_active/.is_anonymous/.get_id
#! class User_Accounts(UserMixin, db.Model):
''''''

class User_Accounts(db.Model):
    __tablename__ = "user_accounts"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    job_position = db.Column(db.String(50))
    current_workflow = db.Column(db.String(50))
    is_admin = db.Column(db.Boolean, default=False, unique=False)
    is_deleted = db.Column(db.Boolean, default=False, unique=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)    

    def __repr__(self):
        return f"User_Accounts(id={self.id!r}, email={self.email!r}, password_hash={self.password_hash!r}"

class Stock_List(db.Model):
    __tablename__ = "stock_list"

    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(70), unique=False)
    quantity = db.Column(db.Integer, default=0, unique=False)
    # lazy defines how database queries for the relationship
    # project = db.relationship('Projects', backref='project_stocks', lazy='dynamic')

    def __repr__(self):
        return f"Stock_List(id={self.id!r}, item={self.item!r}"
    

class Projects(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    # stocks_id = db.Column(ARRAY(db.Integer, db.ForeignKey('stock_list.id')))
    stocks_id = db.Column(db.Integer)
    services_required = db.Column(db.String(50), default="start")
    customer_company = db.Column(db.String(50))
    customer_poc_name = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f"Projects(id={self.id!r}, customer_company={self.customer_company!r}"
    
'''to use back_populates eventually'''
#! backref is getting deprecated soon
''''''

'''populating database without migrate, only sqlalchemy'''
# holds the session
# echo: SQL emitted connections will be logged as standard out.
# future: ensure using SQLAlchemy 2.0 style APIs.

#! engine = create_engine(os.environ['DATABASE_URL'], echo=True, future=True)

# initialise the tables
# Base.metadata.create_all(engine)
''''''
