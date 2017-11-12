# coding: utf-8
from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/home/hello")
def home():
    return render_template('index.html')

if __name__ == '__main__':
	app.run(debug = True)
