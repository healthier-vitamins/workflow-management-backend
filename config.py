import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ['SECRET_KEY'] or 'very-secretive-indeed-failed'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'] or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False