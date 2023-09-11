from flask import Blueprint
from ..controllers.auth_controller import UsuarioController

auth_bp = Blueprint('auth_bp', __name__)

auth_bp.route('/login', methods=['POST'])(UsuarioController.login)
auth_bp.route('/logout', methods=['GET'])(UsuarioController.logout)