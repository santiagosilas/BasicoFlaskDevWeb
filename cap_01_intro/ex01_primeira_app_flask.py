# coding: utf-8
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Site em Construção'

if __name__ == '__main__':
    app.run()

    
