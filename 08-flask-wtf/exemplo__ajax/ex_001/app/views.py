# coding:utf-8
"""
From the Flask docs (http://flask.pocoo.org/docs/0.10/api/#flask.Request.get_json):
"flask.json.jsonify:  creates a response with JSON representation 
of the given arguments with an application/json mimetype
The arguments to this function are the same as to the dict constructor."

Example usage:
from flask import jsonify

@app.route('/_get_current_user')
def get_current_user():
    return jsonify(username=g.user.username,
                   email=g.user.email,
                   id=g.user.id)

This will send a JSON response like this to the browser:
{
    "username": "admin",
    "email": "admin@localhost",
    "id": 42
}


The jsonify() function in flask returns flask.Response() object that already has the 
appropriate content-type header 'application/json' for use with json responses, 
whereas the json.dumps() will just return an encoded string, which would require 
manually adding the mime type header.

JSON encoding and decoding with Python
https://pythonspot.com/en/json-encoding-and-decoding-with-python/

"""


from flask import render_template, request, jsonify
from app import app

records = {1:True, 2:False}

@app.route('/')
@app.route('/samples')
def index():
	return render_template('index.html')

@app.route('/process')
def process():
	info = request.args.get('info')
	return jsonify(result=info)

@app.route('/process2', methods = ['POST']) 
def process2():
	info = request.form['info']
	if len(info.strip()) != 0:
		# Retorna um objeto JSON
		return jsonify(result=info)
	else:
		return jsonify({'error': 'empty!'})


@app.route('/calc_imc', methods = ['GET','POST']) 
def calc_imc():
	if request.method == 'POST':
		try:
			weight = float(request.form['weight'])
			height = float(request.form['height'])
			imc = weight/(height*height)
			# retorna um objeto json
			return jsonify({'imc':imc})
		except ValueError as e:
			return jsonify(error='wrong values', 
				msg = str(e))
		except Exception as e:
			# retorna um objeto json
			return jsonify(error = str(e))
	return render_template('calc_imc.html')

@app.route('/change_status')
def change_status():
	# Obtem o registro
	id_record = int(request.args.get('id_record'))
	
	# Muda o status do registro
	records[id_record] = not records[id_record] 

	# Atualiza na view
	if records[id_record] == True:
		return jsonify(result='paid')
	else:
		return jsonify(result='not paid')
	