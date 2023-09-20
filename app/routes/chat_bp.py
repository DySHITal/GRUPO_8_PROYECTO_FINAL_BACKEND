from flask import Blueprint
from ..controllers.chat_controller import ChatController

chat_bp = Blueprint('chat_bp', __name__)

chat_bp.route('/mensajes', methods=['POST','GET'])(ChatController.getMensajes)