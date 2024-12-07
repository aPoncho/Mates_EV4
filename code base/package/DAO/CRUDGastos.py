from package.DAO.Conexion import Conexion

def obtener_gastos(id):
    try:
        con = Conexion()
        sql = f"SELECT * FROM gastos WHERE id_usuario = '{id}'"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchall()
        con.desconectar()
        return datos
    except Exception as e:
        print("ERROR")
        print(e)
        print("Revise su conexion con la base de datos")

def ingresar_gasto(user_id, monto, descripcion):
    try:
        con = Conexion()
        sql = f"INSERT INTO gastos(id_usuario, monto_gasto,	descripcion) VALUES ('{user_id}', '{monto}', '{descripcion}')"
        con.ejecuta_query(sql)
        con.commit()
        print("datos ingresados satisfactoriamente")
    except Exception as e:
        con.rollback()
        print(e)
        print("Revise su conexion con la base de datos")

