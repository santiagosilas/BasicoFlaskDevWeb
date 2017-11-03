# coding:utf-8
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from app import db

class Nota(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(80))
    conteudo = db.Column(db.Text)
    data_criacao = db.Column(db.DateTime)

    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo
        self.data_criacao = datetime.now()

if __name__ == '__main__':
    db.create_all()
    print(db.metadata.tables)
    print('done.')