from package.DAO.Conexion import Conexion

def obtener_ingresos(id):
    try:
        con = Conexion()
        sql = f"SELECT * FROM ingresos WHERE id_usuario = '{id}'"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchall()
        con.desconectar()
        return datos
    except Exception as e:
        print("ERROR")
        print(e)
        print("Revise su conexion con la base de datos")

def ingresar_ingreso(user_id, monto, fecha, descripcion):
    try:
        con = Conexion()
        sql = f"INSERT INTO ingresos(id_usuario, monto_ingreso, fecha_ingreso, descripcion) VALUES ({user_id}, {monto}, '{fecha}', '{descripcion}')"
        con.ejecuta_query(sql)
        con.commit()
        input("datos ingresados satisfactoriamente")
    except Exception as e:
        con.rollback()
        print(e)
        print("Revise su conexion con la base de datos")