# coding:utf-8

"""
Exemplos de Relacionamentos
Um-para-Um: Uma Nota tem um Atributo
Um-para-Muitos: Quadro possuem Notas
Muitos-para-Muitos: Notas e Etiquetas


http://flask-sqlalchemy.pocoo.org/2.1/models/
"""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from app import db

# Tabela de Associação
notas_etiquetas = db.Table('notas_etiquetas',
    db.Column('etiqueta_id', db.Integer, db.ForeignKey('etiqueta.id')),
    db.Column('nota_id', db.Integer, db.ForeignKey('nota.id'))
)

class Nota(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(80))
    conteudo = db.Column(db.Text)
    dt_criacao = db.Column(db.DateTime)

    # Uma Nota está em apenas um quadro, mas um Quadro pode ter várias notas
    # Relacionamento Um-para-Muitos (Chave estrangeira)
    id_quadro = db.Column(db.Integer, db.ForeignKey('quadro.id'))
    id_atributos = db.Column(db.Integer, db.ForeignKey('atributos.id'))
    atributos = db.relationship('Atributos', backref='nota', uselist=False)

    etiquetas = db.relationship('Etiqueta', secondary=notas_etiquetas, backref=db.backref('nota', lazy='dynamic'))

    def __init__(self, titulo, conteudo, id_quadro, id_atributos):
        self.titulo = titulo
        self.conteudo = conteudo
        self.dt_criacao = datetime.now()
        self.id_quadro = id_quadro
        self.id_atributos = id_atributos


class Quadro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(20))

    # Define uma nova propriedade, que aponta para a classe Nota e carrega várias destas notas.
    # Use o atributo uselist=False para um relacionamento um-para-um
    notas = db.relationship('Nota', backref='quadro', lazy='dynamic')

    def __init__(self, titulo):
        self.titulo = titulo


class Atributos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dt_modificacao =  db.Column(db.DateTime)

    def __init__(self, titulo):
        self.dt_modificacao = datetime.now()

class Etiqueta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20))

    # Qual o impacto em performance ao usar isto ...
    notas = db.relationship('Nota', secondary=notas_etiquetas, backref=db.backref('etiqueta', lazy='dynamic'))

    def __init__(self, nome):
        self.nome = nome



if __name__ == '__main__':

    # Cria o banco de dados sqlite
    db.create_all()

    # Cria os objetos do tipo Quadro
    inbox, actions = Quadro('Inbox'), Quadro('Actions')

    a1 = Atributos(datetime.now())
    a2 = Atributos(datetime.now())
    a3 = Atributos(datetime.now())

    db.session.add(a1)
    db.session.add(a2)
    db.session.add(a3)

    # Adiciona quadros no banco
    db.session.add(inbox)
    db.session.add(actions)
    db.session.commit()

    # Adicionar notas no banco
    n1 = Nota('Estudar Flask', '...', inbox.id, a1.id)
    n2 = Nota('Estudar Flask-SqlAlchemy', '...', inbox.id, a2.id)

    n3 = Nota('Ir na Feira', '...', actions.id, a3.id)
    n3.etiquetas.append(Etiqueta('@home'))
    n3.etiquetas.append(Etiqueta('15 minutos'))
    n3.etiquetas.append(Etiqueta('alra prioridade'))

    print(n3.etiquetas[1].nome)

    db.session.add(n1)
    db.session.add(n2)
    db.session.add(n3)
    db.session.commit()

    # Obtendo os titulos de todas as notas no quadro imbox
    # Três difentes formas. Ambas usam List Comprehensions

    notas_inbox =  db.session.query(Nota).filter(Nota.id_quadro == inbox.id).all()
    titulos = [(nota.titulo) for nota in notas_inbox]
    print(titulos)

    notas_inbox =  Nota.query.filter(Nota.id_quadro == inbox.id).all()
    titulos = [(nota.titulo) for nota in notas_inbox]
    print(titulos)

    titulos = [(nota.atributos.dt_modificacao) for nota in inbox.notas.all()]
    print(titulos)