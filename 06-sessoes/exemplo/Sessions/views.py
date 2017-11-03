# coding:utf-8
from datetime import datetime
from flask import render_template, request, session, redirect, url_for
from Sessions import app


@app.route('/')
@app.route('/home')
def home():
    if session.has_key('user'):
        return render_template('index.html', title='Home Page', year=datetime.now().year, user = session['user'])
    else:
        return redirect(url_for('login'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'flask' and password == 'flask':
            session['user'] = username
            return redirect(url_for('home'))
        else:
            error = 'User or password is invalid!'
    return render_template('login.html', title='Login', year=datetime.now().year, error = error)

@app.route('/logout')
def logout():
    # Remove a sessão do usuário, se existente
    session.pop('user', None)
    return redirect(url_for('home'))