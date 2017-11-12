# coding: utf-8
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    a = 1/0 # ZeroDivisionError: division by zero
    return 'Site em Construção'

if __name__ == '__main__':
    app.run(debug = True)
