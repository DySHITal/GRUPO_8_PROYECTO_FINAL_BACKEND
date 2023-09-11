from ..models.usuario_model import Usuario
from flask import request, session

class UsuarioController:

    @classmethod
    def login(cls):
        data = request.json
        usuario = Usuario(
            correo = data.get('correo'),
            contrasena = data.get('contrasena')
        )

        if Usuario.is_registered(usuario):
            session['alias'] = data.get('alias')
            return {'msg': 'Sesion iniciada'}, 200
        else:
            return {'msg':'Usuario o contraseña incorrectos'}, 401

    @classmethod
    def logout(cls):
        session.pop('alias', None)
        return {'msg':'Sesion cerrada'}, 200