# Primeiro Formulário (Exemplo Básico)
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class FormExemploBasico(Form):
    nome = StringField('nome', 
                       validators=[DataRequired()])
    submit = SubmitField("Enviar")