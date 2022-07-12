from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship
import os

# if a database is initialised, Base shall hold it
Base = declarative_base()

class User_Accounts(Base):
    __tablename__ = "user_accounts"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(120), nullable=False)
    username = Column(String(35), nullable=False)
    password = Column(String(35), nullable=False)
    job_positions = relationship('Job_Positions', back_populates="user_account")
    is_deleted = Column(Boolean, default=False, unique=False)

    def __init__(self, id, first_name, last_name, email, username, password, job_positions, is_deleted):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
        self.job_positions = job_positions
        self.is_deleted = is_deleted
    # represent classes
    def __repr__(self):
        return f"User_Accounts(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, email={self.email!r}, username={self.username!r}, password={self.password!r}, job_positions={self.job_positions!r}, is_deleted={self.is_deleted!r},)"
 

class Job_Positions(Base):
    __tablename__ = "job_positions"

    id = Column(Integer, primary_key=True)
    position = Column(String(35), nullable=False)
    user_account_id = Column(Integer, ForeignKey("user_accounts.id"))
    user_account = relationship('User_Accounts', back_populates="job_positions")

    def __init__(self, id, position, user_account_id, user_account):
        self.id = id
        self.position = position
        self.user_account_id = user_account_id
        self.user_account = user_account
    
    def __repr__(self):
        return f"Job_Positions(id={self.id!r}, position={self.position!r}, user_account_id={self.user_account_id!r}, user_account={self.user_account!r},"

# holds the session
# echo: SQL emitted connections will be logged as standard out.
# future: ensure using SQLAlchemy 2.0 style APIs.

### engine = create_engine(os.environ['DATABASE_URL'], echo=True, future=True)

# initialise the tables
### Base.metadata.create_all(engine)
