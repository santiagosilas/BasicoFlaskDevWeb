# coding: utf-8
from flask import Flask, render_template
from entidades import Usuario

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/contato')
def contato():
    telefone = '(88) 8888-8888'
    email = 'admin@gmail.com'
    endereco = 'Av Washington Soares, 123'
    u = Usuario('Abel', '(88) 8888-8888', 'abel@gmail.com', 
                'M', 'Rua 51', 21, 151, '1234', '1980-08-01', 
                'casado', True)
    return render_template('contato.html',
                           usuario = u)

if __name__ == "__main__":
    app.debug = True
    app.run()