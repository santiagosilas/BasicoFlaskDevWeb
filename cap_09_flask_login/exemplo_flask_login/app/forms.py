# coding:utf-8
from flask_wtf import FlaskForm as Form
from wtforms import TextField, PasswordField, SubmitField

class LoginForm(Form):
    username = TextField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Send')