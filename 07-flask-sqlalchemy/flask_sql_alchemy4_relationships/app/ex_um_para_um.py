# coding:utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# app Flask
app = Flask(__name__)

# Configurações da aplicação
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'a secret key'

# Caminho para a base de dados usada
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///models1to1.db'

# SQLAlchemy monitorará modificações de objetos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Objeto SqlAlchemy
db = SQLAlchemy(app)

class Pessoa(db.Model):
    id = db.Column(
        db.Integer,
        primary_key = True)

    id_telefone = db.Column(
        db.Integer,
        db.ForeignKey('telefone.id'))

    telefone = db.relationship(
        'Telefone',
        backref='pessoa',
        uselist=False)

class Telefone(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True)

if __name__ == '__main__':
    db.create_all()
    p = Pessoa()
    p.telefone = Telefone()
    db.session.add(p)


    print(Pessoa.query.first())
    print(Telefone.query.first())

    tel = p.telefone
    print(tel.pessoa[0])

