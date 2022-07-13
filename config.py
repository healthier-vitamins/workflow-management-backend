import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or "postgresql://office_user:PORKlingto1997@localhost/office_flow_management"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY') or 'very-secretive-indeed-failed'