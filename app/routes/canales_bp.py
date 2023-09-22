from flask import Blueprint
from ..controllers.canales_controller import CanalesController

canal_bp = Blueprint('canal_bp', __name__)

canal_bp.route('/cargar_canales/<int:id_servidor>', methods=['GET'])(CanalesController.getCanales)