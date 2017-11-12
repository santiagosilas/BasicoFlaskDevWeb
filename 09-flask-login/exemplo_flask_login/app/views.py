# coding:utf-8
from flask import render_template, redirect, url_for, request, flash, g
from app import app, db
from app import User, LoginForm, login_manager
from flask_login import login_user, login_required, logout_user, current_user

# This will redirect users to the login view whenever they are required to be logged in
# obs: se este comando estiver no package app (__init__), a informação login_view é perdida (observei durante o debug).
login_manager.login_view = 'login'

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
@app.route('/home')
@login_required
def home():
    return render_template('index.html')

@app.route('/test')
@login_required
def test():
    return render_template('test.html')

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        registered_user = db.session.query(User).filter(User.username==username, User.password==password).first()
        if registered_user is None: 
            flash('erro!')
            return render_template('login.html', form = form)
        else:
            # we will call the login_user function from the Flask-Login extension and 
            # redirect the user to either the index page or the next page the user was 
            # intending to visit.
            login_user(registered_user)
            flash('Logged in successfully')
            next = request.args.get('next')
            return redirect(next or url_for('home'))
    return render_template('login.html', form = form)
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@login_manager.user_loader
def load_user(id):
    """
    user_loader callback - setting how to load the user from an id
    The function loads the user from the database
    obs: ids in Flask-Login are always Unicode strings, so we need to convert them 
    to integers before we can query the data using SQLAlchemy
    """
    # obtem um objeto User.
    return User.query.get(int(id)) 