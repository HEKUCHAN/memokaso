from flask import render_template
from flask.views import MethodView

class LoginView(MethodView):
    def get(self):
        return render_template('login.html')