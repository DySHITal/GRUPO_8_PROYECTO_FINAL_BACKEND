from ..models.chat_model import Chat
from flask import request, session, jsonify

class ChatController:
    
    @classmethod
    def getMensajes(cls):
        data = request.json
        mensaje = Chat(
            canal = data.get('canal')
        )
        if mensaje is not None:
            Chat.get_mensajes(mensaje)
            return {'msg':'Success'}, 200
        else:
            return {'msg':'No hay mensajes'}, 404

    @classmethod
    def postMensajes(cls):
        data = request.json
        message = Chat(
            mensaje = data.get('mensaje'),
            canal = data.get('canal')
        )
        if message is not None:
            Chat.post_mensajes(message)
            return {'msg':'success'}, 200
        else:
            return {'msg':'No hay mensaje'}, 400