# coding:utf-8
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# the flask app
app = Flask(__name__)

# You should create one for your app
login_manager = LoginManager()

# Configure the actual application for login
login_manager.__init__(app)

# base directory
basedir = os.path.abspath(os.path.dirname(__name__))

# app settings
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'asecretkey'

# SqlAlchemy object - created by parsing the application
db = SQLAlchemy(app)

from models import User
from forms import LoginForm
from app import views