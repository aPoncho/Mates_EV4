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

    def agregarUsuario(self, nombre, apellido, email, password, fecha_registro):    
        try:
            sql = f"INSERT INTO usuarios (nombre, apellido, email, password, fecha_registro)" \
                f"VALUES ('{nombre}', '{apellido}', '{email}' '{password}', '{fecha_registro}')"
            self.ejecuta_query(sql)
            self.commit()
            return True
        except Exception as e:
            input(f"Error al ejecutar la consulta. Error: {e} ")
            self.rollback()
            return False