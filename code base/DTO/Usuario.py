class Usuario():
    def __init__(self, nombre, apellido, email, fecha_registro, id = 'NO ID', password = 'NO PASSWORD'):
        self.__id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.__password = password
        self.fecha_registro = fecha_registro

    def bienvenida(self):
        return f'''Bienvenido {self.nombre} {self.apellido}!!'''

    def getId(self):
        return self.__id
    
    def getPassword(self):
        return self.__password
    
    def setId(self, valor):
        self.__id = valor

    def setPassword(self, valor):
        self.__password = valor

    

