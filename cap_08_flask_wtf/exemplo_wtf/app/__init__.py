from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'it is very secret, dud!'

from app import views