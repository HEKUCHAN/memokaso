from flask_login import UserMixin, LoginManager
from memo_app import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(25))
