# Primeiro Formulário (Exemplo Básico)
from flask_wtf import FlaskForm as Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class FormExemploBasico(Form):
    nome = StringField('Nome', 
                       validators=[DataRequired()])
    submit = SubmitField("Enviar")