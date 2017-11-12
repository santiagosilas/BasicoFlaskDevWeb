# coding: utf-8
from flask import Flask
app = Flask(__name__)
app.debug = True
app.secret_key = 'a secret key'
from app import views
