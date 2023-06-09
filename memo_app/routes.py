from memo_app import app
from memo_app.views import *

app.add_url_rule("/", view_func=IndexView.as_view("index"))
app.add_url_rule("/login", view_func=LoginView.as_view("login"))
app.add_url_rule("/signup", view_func=SignupView.as_view("signup"))
