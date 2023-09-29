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

    @classmethod
    def get_mensajes(cls, id_canales):
        try:
            query = """SELECT mensaje FROM tertulia.mensajes WHERE canal = %s"""
            params = (id_canales,)
            result = DatabaseConnection.fetch_all(query, params=params)
            DatabaseConnection.close_connection()
            return result
        except Exception as e:
            raise Exception(e)

    @classmethod
    def post_mensajes(cls, message, id_canal,id_usuario):
        try:
            query = """INSERT INTO tertulia.mensajes(mensaje, fecha_envio, canal)
            VALUES(%(mensaje)s, CURDATE(), %(id_canal)s)"""
            params = {'mensaje':message.mensaje, 'id_canal':id_canal}
            
            DatabaseConnection.execute_query(query, params=params)
        
            # # Obtener el ID del mensaje recién insertado
            # query_get_id = "SELECT LAST_INSERT_ID()"
            # result = DatabaseConnection.execute_query(query_get_id)
            # id_mensaje = result.fetchone()[0]  # Esto obtiene el primer campo del primer resultado
            
            # query2 = """INSERT INTO tertulia.usuario_mensaje(`id_usuario`, `id_mensaje`)
            #             VALUES (%(id_usuario)s,%(id_mensaje)s);"""
            # params2 = {'id_usuario':id_usuario,'id_mensaje': id_mensaje}
            # DatabaseConnection.execute_query(query2, params=params2)
            DatabaseConnection.close_connection()
        except Exception as e:
            raise Exception(e)
        
    @classmethod
    def get_mensajesUsuario(cls, id_usuario):
        try:
            query = """SELECT m.*
                       FROM mensajes m
                       JOIN usuario_mensaje um ON m.id_mensaje = um.id_mensaje
                       WHERE um.id_usuario = %s"""
            params = (id_usuario,)
            result = DatabaseConnection.fetch_all(query, params=params)
            DatabaseConnection.close_connection()
            return result
        except Exception as e:
            raise Exception(e)
     
    @classmethod
    def delete_mensajesUsuario(cls, id_mensaje):
        try:
            query2 = """DELETE FROM usuario_mensaje um 
                       WHERE um.id_mensaje = %s"""
            params2 = (id_mensaje,)
            DatabaseConnection.execute_query(query2, params=params2)
            DatabaseConnection.close_connection()
            query = """DELETE FROM mensajes m
                       WHERE m.id_mensaje = %s"""
            params = (id_mensaje,)
            DatabaseConnection.execute_query(query, params=params)
            DatabaseConnection.close_connection()
           
            return None
        except Exception as e:
            raise Exception(e)   
        
        
    