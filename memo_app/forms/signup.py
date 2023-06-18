from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField
from wtforms.validators import InputRequired, Email, Length, EqualTo


class SignupForm(FlaskForm):
    nickname = StringField(
        "nickname_form",
        validators=[
            InputRequired("必須項目です"),
            Length(min=1, max=15, message="最大15文字です")
        ],
    )
    email = EmailField("email_form", validators=[
        InputRequired("必須項目です。"),
        Email("メールを正しく入力してください。")
    ])
    password = PasswordField("password_form", validators=[
        InputRequired("必須項目です"),
        EqualTo("password_confirm_form", message="パスワードが一致してません。")
    ])
    password_confirm = PasswordField("password_confirm_form", validators=[
        InputRequired("必須項目です。")
    ])

