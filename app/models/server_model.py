from ..database import DatabaseConnection

class Server:

    def __init__(self, **kwargs):
        self.id_servidor = kwargs.get('id_servidor')
        self.nombre_servidor = kwargs.get('nombre_servidor')
        self.fecha_creacion = kwargs.get('fecha_creacion')
        self.descripcion = kwargs.get('descripcion')

    def serialize(self):
        return {
            'id_servidor': self.id_servidor,
            'nombre_servidor': self.nombre_servidor,
            'fecha_creacion': self.fecha_creacion,
            'descripcion': self.descripcion
        }

    @classmethod
    def get_server(cls):
        try:
            query = """SELECT nombre_servidor FROM servidor"""
            result = DatabaseConnection.fetch_all(query)
            if result is not None:
                DatabaseConnection.close_connection()
                return cls(nombre_servidor = result)
            DatabaseConnection.close_connection()
            return None
        except Exception as e:
            raise Exception(e)
    
    @classmethod
    def get_id_server(cls, nombre_servidor):
        try:
            query= "SELECT id_servidor FROM servidor WHERE nombre_servidor = %s"
            result = DatabaseConnection.fetch_one(query,(nombre_servidor,))
            if result is not None:
                DatabaseConnection.close_connection()
                id_servidor = result[0]
                return id_servidor
            DatabaseConnection.close_connection()
            return None
        except Exception as e:
            raise Exception(e)
        
    
    @classmethod
    def get_serverUsuario(cls,usuario): 
        try:                 
            query="""SELECT s.nombre_servidor FROM servidor s
                    JOIN usuario_servidor us ON s.id_servidor = us.servidor
                    JOIN usuarios u ON u.id_usuario = us.usuario
                    WHERE u.correo = %(correo)s;"""
            params = usuario.__dict__
            result = DatabaseConnection.fetch_all(query,params=params)
            if result is not None:
                DatabaseConnection.close_connection()
                return cls(nombre_servidor = result)
            DatabaseConnection.close_connection()
            return None
        except Exception as e:
            raise Exception(e)

    @classmethod
    def create_server(cls, servidor, usuario):
        try:
            query = """
            START TRANSACTION;

            INSERT INTO servidor (nombre_servidor, fecha_creacion, descripcion)
            VALUES (%(server_name)s, CURDATE(), %(server_description)s);

            INSERT INTO usuario_servidor (usuario, servidor) 
            SELECT
                (SELECT id_usuario FROM usuarios WHERE correo = %(correo)s) AS usuario,
                (SELECT id_servidor FROM servidor ORDER BY id_servidor DESC LIMIT 1) AS servidor;

            COMMIT;
            """
            params = {
                'server_name': servidor.nombre_servidor,
                'server_description': servidor.descripcion,
                'correo': usuario.correo
            }
            DatabaseConnection.execute_query(query, params=params)
            DatabaseConnection.close_connection()
        except Exception as e:
            raise Exception(e)

    @classmethod
    def reg_server(cls, id_usuario, id_servidor):
        try:
            query = """INSERT INTO usuario_servidor (usuario, servidor)
            VALUES (%s, %s)"""
            params = (id_usuario, id_servidor)
            DatabaseConnection.execute_query(query, params=params)
            DatabaseConnection.close_connection()
            return None
        except Exception as e:
            raise Exception(e)
        
    @classmethod
    def get_serverUsuarioCreador(cls,id_usuario): 
        try:                 
            query="""SELECT s.nombre_servidor FROM servidor s
                    WHERE id_creador = %s;"""
            params = (id_usuario,)
            result = DatabaseConnection.fetch_all(query,params=params)
            if result is not None:
                DatabaseConnection.close_connection()
                return cls(nombre_servidor = result)
            DatabaseConnection.close_connection()
            return None
        except Exception as e:
            raise Exception(e)

    @classmethod
    def del_server(cls, id_usuario, id_servidor):
        try:
            query = 'DELETE FROM usuario_servidor WHERE usuario = %s AND servidor = %s'
            params = (id_usuario, id_servidor)
            DatabaseConnection.execute_query(query, params=params)
            DatabaseConnection.close_connection()
            return None
        except Exception as e:
            raise Exception(e)
