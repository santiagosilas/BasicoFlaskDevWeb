# coding:utf-8
from flask_wtf import Form
from wtforms import TextField, PasswordField, SubmitField

class LoginForm(Form):
    username = TextField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Send')