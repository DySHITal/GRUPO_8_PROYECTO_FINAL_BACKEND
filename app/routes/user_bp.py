from flask import Blueprint
from ..controllers.user_controller import UsuarioController
from ..controllers.server_controller import ServerController

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/alias', methods=['GET'])(UsuarioController.getAlias)
user_bp.route('/cargar_servidores', methods=['GET'])(ServerController.getServers)
user_bp.route('/servidores_del_usuario', methods=['GET'])(ServerController.getServersUsuario)
user_bp.route('/register', methods=['GET','POST'])(UsuarioController.register)
user_bp.route('/crear_server', methods=['GET','POST'])(ServerController.crearServer)
user_bp.route('/registrar_db/<string:nombre_servidor>', methods=['POST'])(ServerController.regServer)
user_bp.route('/eliminar_server/<string:nombre_servidor>', methods=['DELETE'])(ServerController.delServer)
user_bp.route('/ruta_info_usuario', methods=['GET'])(UsuarioController.getInfo)
user_bp.route('/ruta_servidores_creados/<int:id_usuario>', methods=['GET'])(ServerController.getServersCreador)
user_bp.route('/upload_img', methods=['POST'])(UsuarioController.uploadImg)
user_bp.route('/show_img', methods=['GET'])(UsuarioController.showImg)
