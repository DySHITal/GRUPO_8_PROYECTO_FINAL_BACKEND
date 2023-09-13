from flask import Blueprint
from ..controllers.auth_controller import UsuarioController

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/alias', methods=['GET'])(UsuarioController.getAlias)