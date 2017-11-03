# coding:utf-8
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from app import db
from app.models import Nota

if __name__ == '__main__':

    # Remove todas as notas
    Nota.query.delete()

    # Insere uma nota no banco
    nota = Nota('lembrete 1', 'Estudar Flask-SqlAlchemy')
    db.session.add(nota)
    db.session.commit()

    # Insere uma nota no banco
    nota = Nota('lembrete 2', 'Estudar Flask-WTF')
    db.session.add(nota)
    db.session.commit()

    # Insere uma nota no banco
    nota = Nota('lembrete 3', 'Estudar Flask-Login')
    db.session.add(nota)
    db.session.commit()

    # Insere uma nota no banco
    nota = Nota('lembrete 4', 'Estudar Flask')
    db.session.add(nota)
    db.session.commit()

    # Atualiza uma nota
    nota = nota.query.first()
    nota.titulo = 'lembrete 1 para hoje!'
    db.session.commit()

    # Remove uma nota
    nota = Nota.query.all()[0]
    db.session.delete(nota)
    db.session.commit()

    # Obtém todas as notas
    notas = Nota.query.all()
    for nota in notas:
        print(nota.titulo)

    # Filtrando informações
    notas = Nota.query.filter_by(titulo='lembrete 2').all()
    print('filtro:', notas[0].titulo)


    notas = Nota.query.filter_by(titulo='...').all()
    print('filtro:', notas)

    notas = db.session.query(Nota).filter(Nota.titulo == 'Estudar Flask-SqlAlchemy').first()
    print('filtro:', notas)

    # Obtém todas as notas ordenadas por conteúdo
    notas = Nota.query.order_by(Nota.conteudo)
    for nota in notas:
        print(nota.id, nota.titulo, nota.data_criacao.strftime("%d-%m-%y"))


    notas = Nota.query.filter(Nota.titulo.endswith('3')).all()
    print('consulta 1:', notas[0].titulo)

    nota = Nota.query.filter(Nota.titulo.startswith('lembrete')).first()
    print('consulta 1:', nota.titulo)

    nota = Nota.query.filter(Nota.titulo.contains('lembrete')).first()
    print(nota.titulo)

    nt = Nota.query.get(30)
    if nt is not None:
        print('busca', nt.titulo)
    else:
        print('nota não existente.')

    nt = Nota.query.get(99)
    print('busca', nt)

    nota = Nota.query.filter(Nota.titulo.contains('lembrete'), Nota.conteudo.contains('Flask')).first()
    print(nota.titulo)

