import pymysql
host='localhost'
user='userappdb'
con_password='pass123'
db='appdb'

class Conexion:
    def __init__(self, host = 'localhost', user = 'userappdb', password = 'pass123', db = 'appdb'):
        self.db = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db)
        self.cursor = self.db.cursor()

    def ejecuta_query(self, sql):
        self.cursor.execute(sql)
        return self.cursor

    def desconectar(self):
        self.db.close()

    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()

    def agregarUsuario(self, nombre, apellido, email, hash_password):    
        try:
            sql = f"INSERT INTO usuarios (nombre, apellido, correo, password) VALUES ('{nombre}', '{apellido}', '{email}', '{hash_password}')"
            self.ejecuta_query(sql)
            self.commit()
            return True
        except Exception as e:
            input(f"Error al ejecutar la consulta. Error: {e} ")
            self.rollback()
            return False
        
    def obtener_usuario(self, correo):
        try:
            sql = f"SELECT * FROM usuarios WHERE correo = '{correo}'"
            cursor = self.ejecuta_query(sql)
            datos = cursor.fetchone()
            return datos
        except Exception as e:
            print("ERROR")
            print(e)
            print("Revise su conexion con la base de datos")