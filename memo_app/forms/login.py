from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.validators import InputRequired, Email


class LoginForm(FlaskForm):
    email = EmailField(
        "email_form", validators=[
            InputRequired("必須項目です。"),
            Email("メールを正しく入力してください。")
        ]
    )
    password = PasswordField("password_form", validators=[
        InputRequired("必須項目です")
    ])
