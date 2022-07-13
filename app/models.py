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
    password_hash = db.Column(db.String(35), nullable=False)
    job_position = db.Column(db.String(35))
    current_workflow = db.Column(db.String(35))
    is_admin = db.Column(db.Boolean, default=False, unique=False)
    is_deleted = db.Column(db.Boolean, default=False, unique=False)

    def __repr__(self):
        return f"User_Accounts(id={self.id!r}, username={self.username!r}"

class Stock_List(db.Model):
    __tablename__ = "stock_list"

    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(40))

    def __repr__(self):
        return f"Stock_List(id={self.id!r}, item={self.item!r}"
    

# class Projects(db.Model):
#     __tablename__ = "projects"

#     id = db.Column(db.Integer, primary_key=True)
#     items = db.Column(db.String(50))
#     service = db.Column(db.String(50))
#     customer_company = db.Column(db.String(50))
#     customer_poc_name = db.Column(db.String(50))

#     def __repr__(self):
#         return f"Projects(id={self.id!r}, customer_company={self.customer_company!r}"
    

########################################################################
# holds the session
# echo: SQL emitted connections will be logged as standard out.
# future: ensure using SQLAlchemy 2.0 style APIs.

# engine = create_engine(os.environ['DATABASE_URL'], echo=True, future=True)

# initialise the tables
# Base.metadata.create_all(engine)
