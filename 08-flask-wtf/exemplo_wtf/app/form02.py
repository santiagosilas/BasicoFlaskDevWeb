"""
Campos:

# StringField/TextField: Represents <input type = 'text'> HTML form element
# BooleanField: Represents <input type = 'checkbox'> HTML form element
# DecimalField: Textfield for displaying number with decimals
# IntegerField: TextField for displaying integer
# RadioField: Represents <input type = 'radio'> HTML form element
# SelectField: Represents select form element
# TextAreaField - Represents <testarea> html form element
# PasswordField - Represents <input type = 'password'> HTML form element
# SubmitField - Represents <input type = 'submit'> form element 

Validadores: from wtforms.validators import ...

- DataRequired: Verifica se um campo de entrada é vazio
- Email: Verifica se um texto em um campo segue as convenções de nomeclatura de e-mails
- IPAddress - Valida um endereço IP em um campo de entrada
- Length - Verifica se o tamanho de uma string em um campo de entrada está em um dado range
- NumberRange - Valida um numero no campo de entrada em um dado intervalo
- Valida uma URL informada no campo de entrada
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