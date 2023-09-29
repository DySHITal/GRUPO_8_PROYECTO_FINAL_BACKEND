from ..models.usuario_model import Usuario
from flask import request, session, jsonify
import os
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
        usuario = Usuario.get_info(alias)
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

    @classmethod
    def uploadImg(cls):
        correo = session.get('correo')
        id_usuario = Usuario.get_id_usuario(correo)
        usuario = Usuario(id_usuario=id_usuario)
        if 'avatar' in request.files:
            avatar = request.files['avatar']
            if avatar.filename != "":
                path = os.path.join("app\image", f'user_{id_usuario}.png')
                avatar.save(path)
                usuario.avatar = path
                Usuario.upload_img(usuario)
                return {'msg':'Se cargo el avatar el usuario exitosamente'}, 200
            else:
                return {'msg':'No se cargo el avatar'}, 400
        else:
            return {'msg': 'No se seleccionó ninguna imagen'}, 400

    @classmethod
    def showImg(cls):
        id_usuario = Usuario.get_id_usuario(session.get('correo'))
        usuario = Usuario(id_usuario=id_usuario)
        path = Usuario.show_img(usuario)
        if path is None:
            return {'msg':'Avatar no encontrado'}, 404
        else:
            return path.serialize(), 200
