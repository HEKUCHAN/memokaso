from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField
from wtforms.validators import InputRequired, Email, Length


class SignupForm(FlaskForm):
    nickname = StringField(
        "nickname",
        validators=[InputRequired("必須項目です"), Length(min=1, max=15, message="最大15文字です")],
    )
