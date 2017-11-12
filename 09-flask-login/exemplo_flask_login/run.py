# coding:utf-8

"""
Flask-Login - User session management for Flask
common tasks: logging in, logging out, remembering
based on https://blog.openshift.com/use-flask-login-to-add-user-authentication-to-your-python-application/
"""

from app import app

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    app.run(HOST, PORT)
