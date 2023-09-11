from ..database import DatabaseConnection

class Usuario:
    '''Modelo para la clase usuario'''

    # def __init__(self, id_usuario = None, nombre = None, apellido = None, alias = None, fechas_nacimiento = None, correo = None, contrasena = None, avatar = None, estado = None):
    #     '''Constructor method'''
    #     self.id_usuario = id_usuario
    #     self.nombre = nombre
    #     self.apellido = apellido
    #     self.alias = alias
    #     self.fechas_nacimiento = fechas_nacimiento
    #     self.correo = correo
    #     self.contrasena = contrasena
    #     self.avatar = avatar
    #     self.estado = estado

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
        query = '''SELECT id_usuario FROM tertulia.usuarios WHERE correo = %(correo)s AND contrasena = %(contrasena)s'''
        params = usuario.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)
        print(params)
        print(result)
        if result is not None:
            return True
        return False