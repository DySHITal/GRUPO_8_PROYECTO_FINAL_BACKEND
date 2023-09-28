from ..models.usuario_model import Usuario
from flask import request, session, jsonify
class UsuarioController:

    @classmethod
    def getAlias(cls):
        alias = session.get('correo')
        usuario = Usuario.get_alias(Usuario(correo = alias))
        if usuario is None:
            return {'msg': 'Usuario no encontrado'}, 404
        else:
            return usuario.serialize(), 200
    
    @classmethod
    def getInfo(cls):
        alias = session.get('correo')
        print(alias)
        usuario = Usuario.get_info(alias)
        print(usuario)
        if usuario is None:
            return {'msg': 'Usuario no encontrado'}, 404
        else:
            return usuario.serialize(), 200

    @classmethod
    def register(cls):                  
        data = request.json
        usuario = Usuario(
            correo = data.get('correo'),
            alias = data.get('alias'),
            nombre = data.get('nombre'),
            apellido = data.get('apellido'),
            contrasena = data.get('contrasena'),
            fechas_nacimiento = data.get('fechas_nacimiento'),
            avatar = data.get('avatar')
        )
        if Usuario.is_registered(usuario):
            return {'msg':'Usuario ya registrado'}, 401
        try:
            Usuario.register_user(usuario)
            return jsonify({'msg': 'Usuario Registrado exitosamente'}), 200
        except Exception as e:
            return jsonify({'msg', 'Todos los campos deben estar completados'}), 400