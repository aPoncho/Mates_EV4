import pymysql


class Conexion:
    def __init__(self, host, user, password, db):
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

    def agregarUsuario(self, nombre, apellido, email, password):    
        try:
            sql = f"INSERT INTO usuarios (nombre, apellido, email, password)" \
                f"VALUES ('{nombre}', '{apellido}', '{email}', '{password}')"
            self.ejecuta_query(sql)
            self.commit()
            return True
        except Exception as e:
            input(f"Error al ejecutar la consulta. Error: {e} ")
            self.rollback()
            return False
        
    def obtener_usuario(self, username):
        try:
            sql = f"SELECT * FROM usuarios WHERE username = '{username}'"
            cursor = self.ejecuta_query(sql)
            datos = cursor.fetchone()
            return datos
        except Exception as e:
            print("ERROR")
            print(e)
            print("Revise su conexion con la base de datos")