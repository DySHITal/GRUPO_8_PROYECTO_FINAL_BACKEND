from ..models.usuario_model import Usuario
from ..models.server_model import Server
from flask import request, session, jsonify

class ServerController:

    @classmethod
    def getServers(cls):
        servers = Server.get_server()
        if servers is not None:
            return servers.serialize(), 200
        else:
            return {'msg':'No existen servidores'}, 404

    @classmethod 
    def getServersUsuario(cls):
         alias = session.get('correo')
         servers = Server.get_serverUsuario(Usuario(correo = alias))
         
         if servers is not None:
             return servers.serialize(), 200
         else:
             return {'msg':'Únete a un servidor'}, 404
         
    @classmethod
    def crearServer(cls):
        correo = session.get('correo')
        data = request.json
        servidor= Server(
            nombre_servidor = data.get('server_name'),
            descripcion= data.get('server_descripcion')
        )
        usuario = Usuario(correo=correo)
        if servidor is not None:
            Server.create_server(servidor, usuario)
            return {'msg': 'Server Registrado exitosamente'}, 200
        else:
            return {'msg', 'Todos los campos deben estar completados'}, 400

    