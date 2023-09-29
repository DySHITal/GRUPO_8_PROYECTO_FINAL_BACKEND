from ..models.chat_model import Chat
from ..models.canales_model import Canales
from ..models.usuario_model import Usuario
from ..models.server_model import Server
from flask import request, session, jsonify

class ChatController:
    
    @classmethod
    def getMensajes(cls, nombre_canal):
        id_canales = Canales.get_id_canal(nombre_canal)
        Chat(canal = request.args.get('nombre_canal'))
        mensaje = Chat.get_mensajes(id_canales)
        if mensaje is not None:
            return mensaje, 200
        else:
            return {'msg':'Empty'}

    @classmethod
    def postMensajes(cls):
        data = request.json
        message = Chat(
            mensaje = data['data'].get('mensaje'),
            canal = data['data'].get('canal')
        )
        id_canal = Canales.get_id_canal(message.canal)
        if message is not None:
            Chat.post_mensajes(message, id_canal)
            return {'msg':'success'}, 200
        else:
            return {'msg':'No hay mensaje'}, 400
        
    @classmethod
    def getMensajesUsuario(cls,id_usuario):
        print("todobien")
        print(id_usuario)
        mensajes = Chat.get_mensajesUsuario(id_usuario)
        if mensajes is not None:
            return mensajes, 200
        else:
            return {'msg':'Empty'}
