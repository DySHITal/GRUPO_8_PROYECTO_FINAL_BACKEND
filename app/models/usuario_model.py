from ..database import DatabaseConnection

class Usuario:
    '''Modelo para la clase usuario'''

    def __init__(self, **kwargs):
        self.id_usuario = kwargs.get('id_usuario')
        self.nombre = kwargs.get('nombre')
        self.apellido = kwargs.get('apellido')
        self.alias = kwargs.get('alias')
        self.fechas_nacimiento = kwargs.get('fechas_nacimiento')
        self.correo = kwargs.get('correo')
        self.contrasena = kwargs.get('contrasena')
        self.avatar = kwargs.get('avatar')
        self.estado = kwargs.get('estado')

    def serialize(self):
        '''Serialize object representation
        Returns:
            dict: Object representation '''
        return {
            'id_usuario': self.id_usuario,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'alias': self.alias,
            'fechas_nacimiento': self.fechas_nacimiento,
            'correo': self.correo,
            'contrasena': self.contrasena,
            'avatar': self.avatar,
            'estado': self.estado
        }

    @classmethod
    def is_registered(cls, usuario):
        try:
            query = '''SELECT id_usuario FROM tertulia.usuarios WHERE correo = %(correo)s AND contrasena = %(contrasena)s'''
            params = usuario.__dict__
            result = DatabaseConnection.fetch_one(query, params=params)
            if result is not None:
                DatabaseConnection.close_connection()
                return True
            DatabaseConnection.close_connection()
            return False
        except Exception as e:
            raise Exception(e)

    @classmethod
    def get_alias(cls, usuario):
        try:
            query = """SELECT * FROM tertulia.usuarios 
            WHERE correo = %(correo)s"""
            params = usuario.__dict__
            result = DatabaseConnection.fetch_one(query, params=params)
            if result is not None:
                DatabaseConnection.close_connection()
                return cls(alias = result[3])
            DatabaseConnection.close_connection()
            return None
        except Exception as e:
            raise Exception(e)

        
    @classmethod
    def register_user(cls, usuario):
        try:
            query="""INSERT INTO tertulia.usuarios(nombre, apellido, alias, fechas_nacimiento, correo, contrasena, avatar)
            VALUES(%(nombre)s, %(apellido)s, %(alias)s, %(fechas_nacimiento)s, %(correo)s, %(contrasena)s, %(avatar)s);"""
            params = usuario.__dict__
            DatabaseConnection.execute_query(query, params=params)
            DatabaseConnection.close_connection()
        except Exception as e:
            raise Exception(e)

    @classmethod
    def get_id_usuario(cls, correo):
        try:
            query = 'SELECT id_usuario FROM usuarios WHERE correo = %s'
            result = DatabaseConnection.fetch_one(query, (correo,))
            if result is not None:
                DatabaseConnection.close_connection()
                id_usuario = result[0]
                return id_usuario
            DatabaseConnection.close_connection()
            return None
        except Exception as e:
            raise Exception(e)
            
    @classmethod
    def get_info(cls, correo):    
        try:
            query = """SELECT * FROM tertulia.usuarios 
            WHERE correo = %s"""
            params = (correo,)
            result = DatabaseConnection.fetch_one(query, params=params)
            print(result)
            if result is not None:
                usuario = cls()  # Crear una instancia vacía de Usuario
                usuario.id_usuario=result[0]
                usuario.nombre = result[1]
                usuario.apellido = result[2]
                usuario.alias = result[3]
                usuario.fechas_nacimiento = result[4]
                usuario.correo = result[5]
                # Asignar los valores del resultado a los atributos del usuario
                DatabaseConnection.close_connection()
                return usuario
            DatabaseConnection.close_connection()
            return None
        except Exception as e:
            raise Exception(e)