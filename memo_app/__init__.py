from flask import Flask, render_template
from flask_wtf import CSRFProtect
from flask_wtf.csrf import CSRFError
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from .config import Config


app = Flask(__name__)
app.config.from_object(Config)
csrf = CSRFProtect(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)

with app.app_context():
    db.create_all()

# Load the models
from .models import *

app.url_map.strict_slashes = False


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.errorhandler(CSRFError)
def csrf_error(reason):
    return (render_template("errors/403_csrf.html", reason=reason), 403)

# Load the routing
from .routes import *
