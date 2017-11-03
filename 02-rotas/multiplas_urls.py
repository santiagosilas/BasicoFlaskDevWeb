# coding: utf-8
from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/home/hello")
def hello_world():
	a = 1/0
	return 'Hello World!'

#if __name__ == '__main__':
#	app.config['DEBUG'] = True
#	app.run()

#if __name__ == '__main__':
#	app.debug = True
#	app.run()

if __name__ == '__main__':
	app.run(debug = True)