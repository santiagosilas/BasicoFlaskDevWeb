from TechApp import app
from flask import render_template, redirect, url_for, request

lprodutos = []
lprodutos.append({'id':1, 'nome':'Notebook', 'qtde': 5})
lprodutos.append({'id':2, 'nome':'Macbook', 'qtde': 5})
lprodutos.append({'id':3, 'nome':'Chromebook', 'qtde': 5})
lprodutos.append({'id':4, 'nome':'Teclado', 'qtde': 1})
lprodutos.append({'id':5, 'nome':'Cabo Hdmi', 'qtde': 1})

@app.route('/') 
@app.route('/home')
def homepage():
	usuario = 'Fulano de tal'
	return render_template('index.html', usuario = usuario) 

@app.route('/produtos')
def produtos():
	logado = True # ...
	if logado: 
		return render_template('produtos.html', Lista = lprodutos)
	else:
		return redirect(url_for('homepage'))

@app.route('/produtos/detalhes/<int:id>')
def produto(id):
	p = None
	for item in lprodutos:
		if item['id'] == id:
			p = item
			break
	return render_template('produto.html', produto = p)


@app.route('/produtos/buscar') 
def busca():
	resultado = list()
	termo = request.args['busca']
	for item in lprodutos:
		if termo in item['nome']:
			resultado.append(item)
	return render_template('produtos.html', Lista = resultado)

@app.route('/sobre')
def sobre():
	return render_template('sobre.html', estilo='especial')