from ..database import DatabaseConnection

class Chat:
    
    def __init__(self, **kwargs):
        self.id_mensaje = kwargs.get('id_mensaje')
        self.mensaje = kwargs.get('mensaje')
        self.fecha_envio = kwargs.get('fecha_envio')
        self.canal = kwargs.get('canal')

    def serialize(self):
        return {
            'id_mensaje':self.id_mensaje,
            'mensaje':self.mensaje,
            'fecha_envio':self.fecha_envio,
            'canal':self.canal
        }

    def get_mensajes(cls, mensajes):
        query = """SELECT mensaje FROM tertulia.mensajes WHERE canal = %(mensaje)s"""
        params = mensajes.__dict__
        result = DatabaseConnection.fetch_all(query, params=params)
        return result

    def post_mensajes(cls, mensajes):
        query = """INSERT INTO tertulia.mensajes(mensaje, canal)
        VALUES(%(mensaje)s, %(canal)s, )"""
        params = mensajes.__dict__
        DatabaseConnection.execute_query(query, params=params)