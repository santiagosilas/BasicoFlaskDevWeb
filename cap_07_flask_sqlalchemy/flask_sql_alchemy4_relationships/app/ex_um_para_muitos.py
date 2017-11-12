# coding:utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# app Flask
app = Flask(__name__)

# Configurações da aplicação
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'a secret key'

# Caminho para a base de dados usada
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///models1toN.db'

# SQLAlchemy monitorará modificações de objetos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Objeto SqlAlchemy
db = SQLAlchemy(app)

class Funcionario(db.Model):
    id = db.Column(
        db.Integer,
        primary_key = True)
    id_loja = db.Column(
        db.Integer,
        db.ForeignKey('loja.id'))

class Loja(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True)
    funcs = db.relationship(
        'Funcionario',
        backref='loja',
        lazy='dynamic')


if __name__ == '__main__':
    db.create_all()

    # Exemplo de Uso

    loja = Loja()

    db.session.add(loja)
    db.session.commit()

    func = Funcionario()

    db.session.add(func)
    db.session.commit()

    loja.funcs.append(func)
    loja.funcs.append(Funcionario())
    db.session.commit()

    funcionarios_da_loja = loja.funcs.all()
    loja_func_id = func.loja.id

    print(funcionarios_da_loja)

    print(Funcionario.query.all())

    print(func.loja.id)

    db.session.delete(func)
    db.session.commit()
    print(Funcionario.query.all())

