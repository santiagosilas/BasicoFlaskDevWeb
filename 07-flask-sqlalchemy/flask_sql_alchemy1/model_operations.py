# coding:utf-8
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from app import db
from app.models import Nota

if __name__ == '__main__':

    # Insere uma nota no banco
    nota = Nota('lembrete', 'Estudar Flask-SqlAlchemy')
    db.session.add(nota)
    db.session.commit()

    # Atualiza uma nota
    nota.titulo = 'Estudar Flask-SqlAlchemy'
    db.session.commit()

    # Atualiza uma nota
    nota = Nota.query.all()[0]
    db.session.delete(nota)
    db.session.commit()

    # Obtém todas as notas
    notas = Nota.query.all()
    for nota in notas:
        print(nota.titulo)

    # Filtrando informações
    notas = Nota.query.filter_by(titulo='Estudar Flask-SqlAlchemy').all()
    print(notas[0].titulo)

    notas = Nota.query.filter_by(titulo='...').all()
    print(notas)