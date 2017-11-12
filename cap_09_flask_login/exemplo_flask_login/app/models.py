# coding:utf-8
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from app import db

class User(db.Model):
    """
    @summary: A User class that extends the SQLAlchemy db.Model class
    For authentication we need a User model class that will store the username 
    and password associated with a user
    """
    # We have explicitly specified the name of the table as users. 
    # If we don’t specify any table name, the name of the table will be user
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique=True, index=True)
    password = db.Column(db.String(10))
    email = db.Column(db.String(50),unique=True , index=True)
    registered_on = db.Column(db.DateTime)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.date = datetime.now()

    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return self.id
 
    def __repr__(self):
        return '<User %r>' % (self.username)