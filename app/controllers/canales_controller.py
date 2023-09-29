from ..models.canales_model import Canales
from ..models.server_model import Server
from ..models.chat_model import Chat
from flask import request, session, jsonify

class CanalesController:

    @classmethod
    def getCanales(self, nombre_servidor):
        id_servidor = Server.get_id_server(nombre_servidor)
        Canales(id_servidor = request.args.get('id_servidor'))
        canal = Canales.get_canales(id_servidor)
        if canal is not None:
            return canal, 200
        else:
            return {'msg':'No hay canales'} 
    
    @classmethod
    def crearCanal(cls, nombre_servidor):
        data = request.json
        id_servidor = Server.get_id_server(nombre_servidor)
        nombre_canal = data.get('nombre_canal')
        if nombre_canal is not None:
            Canales.crear_canal(nombre_canal, id_servidor)
            return {'msg': 'Canal creado exitosamente'}, 200
        else:
            return {'msg':'Error al crear el canal'}, 400