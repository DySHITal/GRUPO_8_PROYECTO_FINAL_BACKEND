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
        if usuario is not None:
            Usuario.register_user(usuario)
            return jsonify({'msg': 'Usuario Registrado exitosamente'}), 200
        else:
            return jsonify({'msg', 'Todos los campos deben estar completados'}), 400