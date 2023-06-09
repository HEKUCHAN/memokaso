from flask import render_template
from flask.views import MethodView

class SignupView(MethodView):
    def get(self):
        return render_template('signup.html')
