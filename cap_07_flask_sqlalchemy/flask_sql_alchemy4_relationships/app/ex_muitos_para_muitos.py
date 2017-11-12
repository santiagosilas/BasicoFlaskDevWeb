# coding:utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# app Flask
app = Flask(__name__)

# Configurações da aplicação
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'a secret key'

# Caminho para a base de dados usada
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///modelsNtoN.db'

# SQLAlchemy monitorará modificações de objetos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Objeto SqlAlchemy
db = SQLAlchemy(app)

# Tabela de Associação que é usada para o relacionamento
matriculas = db.Table('matriculas',
    db.Column('aluno_id',
              db.Integer,
              db.ForeignKey('aluno.id')),

    db.Column('disciplina_id',
              db.Integer,
              db.ForeignKey('disciplina.id'))
)

class Aluno(db.Model):

    id = db.Column(
        db.Integer,
        primary_key = True)

    disciplinas = db.relationship(
        'Disciplina',
        secondary=matriculas,
        backref=db.backref(
            'aluno',
            lazy='dynamic'))

class Disciplina(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True)

    alunos = db.relationship(
    'Aluno',
    secondary=matriculas,
    backref=db.backref(
        'disciplina',
        lazy='dynamic'))

if __name__ == '__main__':
    db.create_all()
    a1 = Aluno()
    a2 = Aluno()
    a3 = Aluno()

    db.session.add(a1)
    db.session.add(a2)
    db.session.add(a3)
    db.session.commit()

    d1 = Disciplina()
    d2 = Disciplina()

    db.session.add(d1)
    db.session.add(d2)
    db.session.commit()

    a1.disciplinas.append(d1)
    a1.disciplinas.append(d2)

    a2.disciplinas.append(d1)
    a2.disciplinas.append(d2)

    db.session.commit()

    for a in Aluno.query.all():
        for d in a.disciplinas:
            print('Aluno',a.id,'Disciplina', d.id)



