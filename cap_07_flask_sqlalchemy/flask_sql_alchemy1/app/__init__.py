import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurações da aplicação
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'a secret key'

# Caminho para a base de dados usada
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///models.db'

# SQLAlchemy monitorará modificações de objetos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Objeto SqlAlchemy
db = SQLAlchemy(app)

from app import views