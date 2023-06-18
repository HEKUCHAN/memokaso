from flask import render_template
from flask.views import MethodView

from memo_app import db
from memo_app.forms import SignupForm
from memo_app.models import User

class SignupView(MethodView):
    def __init__(self):
       self.form = SignupForm()
       self.user_model = User

    def get(self):
        return render_template("signup.html", form=self.form)

    def post(self):
        if self.form.validate_on_submit():
            user = self.user_model(
                self.form.nickname.data,
                self.form.email.data,
                self.password.data
            )
            db.session.add(user)
            
        

