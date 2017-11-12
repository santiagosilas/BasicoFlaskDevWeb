# coding: utf-8
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return render_template('index.html')

@app.route("/contato")
@app.route("/home/contato")
def contato():
	return render_template('contato.html')

if __name__ == '__main__':
	app.run(debug = True)
