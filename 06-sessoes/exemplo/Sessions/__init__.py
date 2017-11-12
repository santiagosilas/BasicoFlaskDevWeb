"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
app.debug = True
app.secret_key = 'a very secret key'

import Sessions.views
