import bcrypt
from package.DAO.Conexion import Conexion
import time

class Usuario():
    def __init__(self, nombre, apellido, email, fecha_registro = time.time() , id = 'NO ID', password = 'NO PASSWORD'):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
        self.fecha_registro = fecha_registro

    def bienvenida(self):
        return f'''Bienvenido {self.nombre} {self.apellido}!!'''
    

    def registrar_usuario(self):
        try:
            host='localhost'
            user='userappdb'
            password_con='pass123'
            db='appdb'
            self.password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())

            con = Conexion(host, user, password_con, db)
            exito = con.agregarUsuario(self.nombre, self.apellido, self.email, self.password)

            if exito:
                print("¡Usuario registrado exitosamente!") 
            
            else:
                print("Error al registrar el usuario.")
                return None
        except Exception as e:
            input(f'{e} \n Presione cualquier tecla para continuar')
            return None

    @staticmethod
    def login(username, password):
        host='localhost'
        user='userempresa'
        con_password='V3ntana.13'
        db='empresa'
        try:
            con = Conexion(host, user, con_password, db)
            usuario_data = con.obtener_usuario(username)
            if usuario_data:
                hashed_password = usuario_data[2].encode('utf-8')
                
                if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                    return Usuario(
                        nombre = usuario_data[3],
                        apellido = usuario_data[4],
                        correo = usuario_data[5],
                        username = usuario_data[1],
                        password_hash = usuario_data[2],
                        tipo_usuario = usuario_data[6]
                    )
            else:    
                return None
        except Exception as e:
            print ('ERROR')
            print(e)
            return None

