# coding: utf-8
from app import app
from flask import Flask, request, render_template,redirect, url_for
from app.entidades import Usuario, GerenciarUsuarios

contexto = GerenciarUsuarios()

estados_civis = {
    'solteiro': 'SOLTEIRO(A)',
    'casado': 'CASADO(A)',
    'viúvo':'VIÚVO(A)',
    'divorciado':'DIVORCIADO(A)' }

@app.route('/')
@app.route('/home')
def home():
    data = contexto.ListarUsuarios()
    return render_template('index.html',
                            logado = True,
                            usuarios = data)

@app.route('/usuario/buscar')
def usuario_buscar():
    busca, filtro = request.args.get('busca_usuario'), list()
    data = contexto.ListarUsuarios()
    for u in data:
        if busca.upper() in u.nome.upper():
            filtro.append(u)

    return render_template('index.html',
                            logado = True,
                            usuarios = filtro)



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
        u.endereco.logradouro = request.form['logradouro']
        u.endereco.numero = request.form['numero']
        u.endereco.complemento = request.form['complemento']
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