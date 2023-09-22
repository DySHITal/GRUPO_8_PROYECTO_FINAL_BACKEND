from ..database import DatabaseConnection

class Canales:

    def __init__(self, **kwargs):
        self.id_canales = kwargs.get('id_canales')
        self.nombre_canal = kwargs.get('nombre_canal')
        self.id_servidor = kwargs.get('id_servidor')

    def serialize(self):
        return {
            'id_canales': self.id_canales,
            'nombre_canal': self.nombre_canal,
            'id_servidor': self.id_servidor
        }

    @classmethod
    def get_canales(cls, id_servidor):
        try:
            query = 'SELECT nombre_canal FROM canales WHERE id_servidor = %s'
            params = (id_servidor,)
            result = DatabaseConnection.fetch_all(query, params)
            if result is not None:
                DatabaseConnection.close_connection()
                return result
            DatabaseConnection.close_connection()
            return None
        except Exception as e:
            raise Exception(e)