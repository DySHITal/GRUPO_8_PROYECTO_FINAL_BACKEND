from ..models.canales_model import Canales
from ..models.server_model import Server
from flask import request, session, jsonify

class CanalesController:

    @classmethod
    def getCanales(self, nombre_servidor):
        print(nombre_servidor)
        id_servidor = Server.get_id_server(nombre_servidor)
        print(id_servidor)
        Canales(id_servidor = request.args.get('id_servidor'))
        canal = Canales.get_canales(id_servidor)
        if canal is not None:
            print(canal)
            return canal, 200
        else:
            return {'msg':'No hay canales'} 