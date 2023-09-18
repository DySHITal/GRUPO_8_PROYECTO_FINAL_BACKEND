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

    # @classmethod ---- es lo mismo que la función anterior
    # def getServersUsuario(cls):
    #     servers = Server.get_server()
    #     if servers is not None:
    #         return servers.serialize(), 200
    #     else:
    #         return {'msg':'Únete a un servidor'}, 404