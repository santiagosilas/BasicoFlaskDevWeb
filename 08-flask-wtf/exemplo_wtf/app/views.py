from app import app
from flask import render_template
from datetime import datetime
import os

from werkzeug.utils import secure_filename

from app.form01 import FormExemploBasico
from app.form02 import FormRegistro

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/form01', methods=('GET', 'POST'))
def view01():
    form = FormExemploBasico()
    if form.validate_on_submit():
        nome = form.nome.data
        return "Olá, " + nome
    return render_template('form01.html', 
                           form=form)

@app.route('/')
@app.route('/form02', methods=('GET', 'POST'))
def view02():
    form = FormRegistro()
    campos = list()
    if form.validate_on_submit():
        # coleta os campos do formulário
        nome = form.nome.data
        email = form.email.data

        # salva o arquivo em ../static/photos/
        f = form.photo.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.static_folder, 'photos', filename))

    return render_template('form02.html', form=form)