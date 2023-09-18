from flask import Blueprint
from ..controllers.auth_controller import UsuarioController
from ..controllers.server_controller import ServerController

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/alias', methods=['GET'])(UsuarioController.getAlias)
user_bp.route('/cargar_servidores', methods=['GET'])(ServerController.getServers)
# user_bp.route('/servidores_del_usuario', methods=['GET'])(ServerController.getServersUsuario) -- es lo mismo que /cargar_servidores