from ..models.usuario_model import Usuario
from ..models.server_model import Server
from flask import request, session, jsonify

class UsuarioController:

    @classmethod
    def login(cls):
        data = request.json
        usuario = Usuario(
            correo = data.get('correo'),
            contrasena = data.get('contrasena'),
        )

        if Usuario.is_registered(usuario):
            session['correo'] = data.get('correo')
            return {'msg': 'Sesion iniciada'}, 200
        else:
            return {'msg':'Usuario o contraseña incorrectos'}, 401

    @classmethod
    def logout(cls):
        session.pop('alias', None)
        return {'msg':'Sesion cerrada'}, 200

    @classmethod
    def getAlias(cls):
        alias = session.get('correo')
        usuario = Usuario.get_alias(Usuario(correo = alias))
        if usuario is None:
            return {'msg': 'Usuario no encontrado'}, 404
        else:
            return usuario.serialize(), 200

    @classmethod
    def register(cls):                  #recibe fechas_nacimiento como NULL...
        data = request.json
        usuario = Usuario(
            correo = data.get('correo'),
            alias = data.get('alias'),
            nombre = data.get('nombre'),
            apellido = data.get('apellido'),
            contrasena = data.get('contrasena'),
            fechas_nacimiento = data.get('date')
        )
        if usuario is not None:
            Usuario.register_user(usuario)
            return {'msg': 'Usuario Registrado exitosamente'}, 200
        else:
            return {'msg', 'Todos los campos deben estar completados'}
    
