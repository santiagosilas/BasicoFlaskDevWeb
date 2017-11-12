# coding:utf-8
from __future__ import unicode_literals

class Endereco:
    def __init__(self, logradouro, numero,
                 complemento):
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento

class Usuario:
    def __init__(self, nome, tel,
                 email, sexo, log,
                 num, comp, senha,
                 data_nasc,
                 estado_civil,
                 notificar_me):
        self.id = None
        self.nome = nome
        self.telefone = tel
        self.email = email
        self.sexo = sexo
        self.endereco = Endereco(log,
                                 num,
                                 comp)
        self.senha = senha
        self.data_nasc = data_nasc
        self.estado_civil = estado_civil
        self.notificar_me = notificar_me


class GerenciarUsuarios:
    def __init__(self):
        self.key = 1
        self.usuarios = dict()

        u_1 = Usuario('Abel', '(88) 8888-8888', 'abel@gmail.com', 'M', 'Rua 51', 21, 151, '1234', '1980-08-01',
                      'casado', True)
        u_2 = Usuario('Joseph', '(88) 8888-8888', 'joseph@gmail.com', 'M', 'Rua 42', 22, 152, '1234', '1980-08-01',
                      'viúvo', True)
        u_3 = Usuario('Maria', '(88) 8888-8888', 'maria@gmail.com', 'F', 'Rua 33', 23, 153, '1234', '1980-08-01',
                      'solteiro', True)
        u_4 = Usuario('Eva', '(88) 8888-8888', 'eva@gmail.com', 'F', 'Rua 24', 24, 154, '1234', '1980-08-01', 'casado',
                      True)
        u_5 = Usuario('Frank', '(88) 8888-8888', 'frank@gmail.com', 'M', 'Rua 15', 25, 155, '1234', '1980-08-01',
                      'solteiro', True)

        self.InserirUsuario(u_1)
        self.InserirUsuario(u_2)
        self.InserirUsuario(u_3)
        self.InserirUsuario(u_4)
        self.InserirUsuario(u_5)

    def InserirUsuario(self, usuario):
        usuario.id = self.key
        self.usuarios[self.key] = usuario
        self.key += 1

    def ListarUsuarios(self):
        return self.usuarios.values()

    def UsuarioExiste(self, id):
        return self.usuarios.__contains__(id)

    def BuscarUsuario(self, id):
        if self.usuarios.__contains__(id):
            return self.usuarios[id]
        else:
            return None

    def RemoverUsuario(self, id):
        d = dict()
        if self.usuarios.__contains__(id):
            del self.usuarios[id]


if __name__ == '__main__':
    contexto = GerenciarUsuarios()
    contexto.RemoverUsuario(4)
    u = contexto.usuarios[1]
    u.nome = 'Matheus'
    for usuario in contexto.ListarUsuarios():
        print(usuario.id, usuario.nome)
    u = contexto.BuscarUsuario(2)
    print(u.nome)

    print('done.')