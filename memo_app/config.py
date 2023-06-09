import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', default=os.urandom(24))
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_URI', default="sqlite:///memo.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
