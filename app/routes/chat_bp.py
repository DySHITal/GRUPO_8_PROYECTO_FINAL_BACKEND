from flask import Blueprint
from ..controllers.chat_controller import ChatController

chat_bp = Blueprint('chat_bp', __name__)

chat_bp.route('/mensajes/<string:nombre_canal>', methods=['GET'])(ChatController.getMensajes)
chat_bp.route('/mensajes', methods=['POST'])(ChatController.postMensajes)

chat_bp.route('/ruta_mensajes_enviados/<int:id_usuario>',methods=['GET'])(ChatController.getMensajesUsuario)