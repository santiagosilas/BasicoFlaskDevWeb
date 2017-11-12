from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from TechApp import db

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
    titulo = db.Column(db.String(20))    
    funcs = db.relationship(
        'Funcionario',
        backref='loja',
        lazy='dynamic')
    def __init__(self, t):
        self.titulo = t

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

matriculas = db.Table(
    
    'matriculas',
    
    db.Column('aluno_id',
            db.Integer,
            db.ForeignKey('aluno.id')),
    
    db.Column('disciplina_id',
            db.Integer,
            db.ForeignKey('disciplina.id')) )



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

obter_lojas = lambda: Loja.query.all()

def inserir_loja(titulo):
    loja = Loja(titulo)
    db.session.add(loja)
    db.session.commit()

def atualizar_loja(id, titulo):
    loja = Loja.query.get(id)
    if loja is not None:
        loja.titulo = titulo
        db.session.commit()
    else:
        raise Exception('Loja nao existe!')

def remover_loja(id):
    loja = Loja.query.get(id)
    if loja:
        db.session.delete(loja)
        db.session.commit()
        return True
    else:
        return False