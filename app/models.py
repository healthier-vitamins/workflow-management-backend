# from sqlalchemy import db.Boolean, Column, db.Integer, db.String, ForeignKey, create_engine
# from sqlalchemy.orm import declarative_base, relationship

# if a database is initialised, Base shall hold it
# Base = declarative_base()

from app import db

class User_Accounts(db.Model):
    __tablename__ = "user_accounts"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(35), nullable=False, unique=True)
    password_hash = db.Column(db.String(35), nullable=False)
    job_position = db.Column(db.String(35), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False, unique=False)
    current_workflow = db.Column(db.String(35))

    # def __init__(self, id, first_name, last_name, email, username, password, job_positions, is_deleted):
    #     self.id = id
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.email = email
    #     self.username = username
    #     self.password = password
    #     self.job_positions = job_positions
    #     self.is_deleted = is_deleted
    
    # represent classes
    def __repr__(self):
        return f"User_Accounts(id={self.id!r}, username={self.username!r}"

class Stocks(db.Model):
    __tablename__ = "stocks"

    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(40))

    def __repr__(self):
        return f"Stocks(id={self.id!r}, item={self.item!r}"
    

# class Projects(db.Model):
#     __tablename__ = "projects"

#     id = db.Column(db.Integer, primary_key=True)
#     customer_company = db.Column(db.String(50))
#     customer_poc_name = db.Column(db.String(50))


# holds the session
# echo: SQL emitted connections will be logged as standard out.
# future: ensure using SQLAlchemy 2.0 style APIs.

# engine = create_engine(os.environ['DATABASE_URL'], echo=True, future=True)

# initialise the tables
# Base.metadata.create_all(engine)
