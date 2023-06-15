from flask_login import login_user
from flask.views import MethodView
from flask import render_template, request, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash

from memo_app import User
from memo_app.forms import LoginForm


class LoginView(MethodView):
    def __init__(self):
        self.form = LoginForm()

    def get(self):
        return render_template("login.html", form=self.form)

    def post(self):
        email = request.form.get("email")
        password = request.form.get("password")

        print("email:", email)
        print("password:", password)

        if self.form.validate_on_submit():
            user = User.query.filter_by(email=email).first()

            if not user is None and check_password_hash(user.password, password):
                login_user(user)
                return redirect("/")
            else:
                print("- メールまたはパスワードが間違っています。")
                flash("メールまたはパスワードが間違っています。")

        return render_template("login.html", form=self.form)
