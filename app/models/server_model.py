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
        query = """SELECT nombre_servidor FROM servidor"""
        result = DatabaseConnection.fetch_all(query)
        if result is not None:
            return cls(nombre_servidor = result)
        return None
    
    @classmethod
    def get_serverUsuario(cls,usuario):                  #no está implementado
        query="""SELECT s.nombre_servidor FROM servidor s
                 JOIN usuario_servidor us ON s.id_servidor = us.servidor
                 JOIN usuarios u ON u.id_usuario = us.usuario
                 WHERE u.correo = %(correo)s;"""
        params = usuario.__dict__
        result = DatabaseConnection.fetch_all(query,params=params)
        
        if result is not None:
            return cls(nombre_servidor = result)
        return None        