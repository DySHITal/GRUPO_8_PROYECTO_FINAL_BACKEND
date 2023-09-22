from ..models.canales_model import Canales
from flask import request, session, jsonify

class CanalesController:

    @classmethod
    def getCanales(self, id_servidor):
        Canales(id_servidor = request.args.get('id_servidor'))
        canal = Canales.get_canales(id_servidor)
        if canal is not None:
            return canal, 200
        else:
            return {'msg':'No hay canales'} 