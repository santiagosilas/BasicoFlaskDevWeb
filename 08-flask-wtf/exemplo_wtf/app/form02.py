"""
Campos:
    # StringField/TextField: Representa um <input type = 'text'>
    # BooleanField: <input type = 'checkbox'>
    # DecimalField: Textfield para números com decimais
    # IntegerField: TextField para Inteiros
    # RadioField: <input type = 'radio'>
    # SelectField: <select>
    # TextAreaField: <testarea>
    # PasswordField: <input type = 'password'>
    # SubmitField: <input type = 'submit'> 

Validadores: from wtforms.validators import ...
    # DataRequired: Verificar se um campo de entrada é vazio.
    # Email: Verifica se um texto é um e-mail válido
    # Length: Verifica se o tamanho da string está em um dado range
"""

# Formulário de Cadastro

from flask_wtf import FlaskForm as Form

# campos
from wtforms import StringField, RadioField, TextAreaField, \
    IntegerField, PasswordField, SubmitField, SelectField, \
    BooleanField, DateField, FloatField, DecimalField, DateTimeField

# validadores
from wtforms.validators import DataRequired, Email, Length, Required

# para arquivos
from flask_wtf.file import FileField, FileAllowed, FileRequired

from werkzeug.utils import secure_filename

class FormRegistro(Form):
    
    # Caixa de Texto
    nome = StringField("Nome", 
                       [
                           DataRequired("Informe teu nome"), 
                           Length(min=4, max=25)
                       ])

    # Caixa de Texto
    email = StringField("Email", 
                        [
                            DataRequired("Informe teu e-mail"), 
                            Email("Informa teu e-mail")
                        ])
    
    # Caixa de  Texto para Senha (Input type="password")
    senha = PasswordField('Senha',
                          validators=[DataRequired()])

    # Caixa de Texto para valor inteiro
    idade = IntegerField("Idade")
    
    # Caixa de Texto para valor ponto flutuante
    peso = FloatField("Peso")
    
    # Radio
    sexo = RadioField('Sexo', 
                      choices = [
                          ('M','Masculino'), 
                          ('F','Feminino')
                      ])
    
    # TextArea
    endereco = TextAreaField("Endereco",
                             validators=[DataRequired()])
    

    # Select
    estado_civil = SelectField('Estado Civil',
                               choices = [
                                   ('S', 'Solteiro'), 
                                   ('C', 'Casado'), 
                                   ('V', 'Viuvo')
                               ])

    # checkbox
    aceite = BooleanField('Eu aceito os termos de serviço',
                          [DataRequired()])
    
    # Data
    dt = DateTimeField('Data de Nascimento',
                       format='%d/%m/%Y %H:%M',
                       validators = [
                           DataRequired("Informe a data: dd/mm/aaaa hh:mm")
                       ])

    # photo
    photo = FileField('Image',
                      validators=[FileRequired(),
                                  FileAllowed(['jpg', 'png'],
                                              'Apenas imagens!')])

    # botão submit
    submit = SubmitField("Enviar")