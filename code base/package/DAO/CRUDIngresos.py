from package.DAO.Conexion import Conexion

def obtener_ingresos(self, correo):
    try:
        sql = f"SELECT * FROM ingresos WHERE id_usuario = '{correo}'"
        cursor = self.ejecuta_query(sql)
        datos = cursor.fetchall()
        return datos
    except Exception as e:
        print("ERROR")
        print(e)
        print("Revise su conexion con la base de datos")

