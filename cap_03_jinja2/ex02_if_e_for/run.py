# exemplo
from flask import Flask, request, render_template,redirect, url_for

from entidades import Usuario, GerenciarUsuarios, estados_civis

app = Flask(__name__)

contexto = GerenciarUsuarios()

@app.route('/')
@app.route('/home')
def home():
    data = contexto.ListarUsuarios()
    return render_template('index.html',
                            logado = True, 
                            usuarios = data)

@app.route('/contato')
def contato():
    telefone = '(88) 8888-8888'
    email = 'admin@gmail.com'
    endereco = 'Av Washington Soares, 123'
    u = Usuario('Abel', '(88) 8888-8888', 'abel@gmail.com', 'M', 'Rua 51', 21, 151, '1234', '1980-08-01', 'casado', True)
    return render_template('contato.html',
                           logado = True, 
                           usuario = u)

@app.route("/usuario/detalhes/<int:id>")
def usuario_detalhes(id):
    u = contexto.BuscarUsuario(id)
    if u is not None:
        return render_template('usuario_detalhes.html', 
                                logado = True, 
                                usuario = u)
    return 'usuário inexistente'

@app.route("/usuario/remover/<int:id>")
def usuario_remover(id):
    if contexto.UsuarioExiste(id):
        contexto.RemoverUsuario(id)
        return redirect(url_for('home'))
    return 'usuário inexistente'

@app.route("/usuario/atualizar/<int:id>", 
    methods = ['GET', 'POST'])
def usuario_atualizar(id):
    if request.method == 'GET':
        u = contexto.BuscarUsuario(id)
        if u is not None:
            return render_template('usuario_atualizar.html', 
                                    usuario = u, 
                                    logado = True,
                                    estados_civis = estados_civis)
        else:
            return redirect(url_for('home'))
    else:
        u = contexto.BuscarUsuario(id)

        u.nome = request.form['nome']
        u.telefone = request.form['telefone']
        u.email = request.form['email']
        u.logradouro = request.form['logradouro']
        u.numero = request.form['numero']
        u.complemento = request.form['complemento']
        u.senha = request.form['senha']
        u.sexo = request.form['sexo']
        u.notificar_me = "notificar_me" in request.form
        u.data_nasc = request.form['data_nasc']
        u.estado_civil = request.form.get('estado_civil')

        return redirect(url_for('home'))


@app.route("/usuario/inserir/",
           methods=['GET', 'POST'])
def usuario_inserir():
    if request.method == 'POST':
        # obtém os campos do formulário
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']
        log = request.form['logradouro']
        num = request.form['numero']
        comp = request.form['complemento']
        senha = request.form['senha']
        sexo = request.form['sexo']
        notificar_me = "notificar_me" in request.form
        data_nasc = request.form['data_nasc']
        estado_civil = request.form.get('estado_civil')

        # insere o usuário
        u = Usuario(nome,telefone,email, sexo, log, 
                    num,comp, senha,data_nasc, 
                    estado_civil,notificar_me )
        contexto.InserirUsuario(u)

        # redireciona para a página inicial
        return redirect(url_for('home'))

    return render_template('usuario_inserir.html', 
                            logado = True,
                            estados_civis = estados_civis)

@app.route('/buscar')
def u_buscar ( ):
    busca = request.args['search']
    busca = request.args.get('search', 'valor default')

    return busca

@app.route('/buscar/get')
def u_buscar_get ( ):
    return render_template('u_buscar_get.html', logado = True)

@app.route('/buscar/post', methods=['GET', 'POST'])
def u_buscar_post ( ):
    if request.method == 'POST':
        busca = request.form['search']
        busca = request.form.get('search', 'valor default') 
        return busca
    return render_template('u_buscar_post.html', logado = True)   

@app.route('/produto/id')
@app.route('/produto/id/<int:id>')
def produto(id = None):
    if id is not None:
        return 'produto {}'.format(id)
    return 'produto não existe'

if __name__ == "__main__":
    app.debug = True
    app.run()