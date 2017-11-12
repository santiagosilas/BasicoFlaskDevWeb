# exemplo
from flask import Flask, render_template

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
    return render_template('contato.html',
                           tel = telefone,
                           email = email,
                           end = endereco)



if __name__ == "__main__":
    app.debug = True
    app.run()