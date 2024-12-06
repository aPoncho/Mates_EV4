import os
from time import sleep
from getpass import getpass
from package.DTO.Usuario import Usuario
from package.DAO.Conexion import Conexion
from getpass import getpass

host='localhost'
user='userappdb'
password='pass123'
db='appdb'

def menu_login():
    while True:
        os.system('cls')
        opcion = input("""
================================
    M E N Ú  P R I N C I P A L
================================
        1.- LOGIN
        2.- REGISTRO
        3.- SALIR
================================\n""")
        
        if opcion == '1':
            user = login()
            if user is not None:
                print(user.nombre)
                input()
                #ESTA WEA NO QUIERE ROMPER EL BUCLE POR ALGUN MOTIVO
                return user
               

        elif opcion == '2':
            registrar_usuario()
        elif opcion == '3':
            confirm = input("¿Está seguro que desea salir? si/no")
            if confirm.lower() == 'si':
                print('Hasta luego!')
                sleep(1)
                exit()
            else:
                input(f'algo pasa con {user}')
                continue
        else:
            input("Opcion fuera de rango, presione cualquier tecla")


    
def login():
    os.system("cls")
    print("================================")
    print("       LOGIN DE USUARIO       ")
    print("================================")
    
    while True:
        try:
            username = input("Ingrese nombre de usuario: ")
            password = getpass("Ingrese contraseña: ")
            user = Usuario.login(username, password)           
            if user:
                os.system("cls")
                input(f"{user.bienvenida()} \n PRESIONE UNA TECLA PARA CONTINUAR")
                return user
            else:
                input('Usuario y/o contraseña incorrectos, Presione cualquier tecla')
                return None

        except:
            input("ERROR INESPERADO")


def registrar_usuario():
    
    
    while True:
        os.system("cls")
        print("================================")
        print("      REGISTRO DE USUARIO       ")
        print("================================")
        # host='localhost'
        # user='userappdb'
        # password_con='pass123'
        # db='appdb'
        # while True:
        #     username = input('Ingrese nombre de usuario: ')
        #     if username == '' or ' ' in username:
        #         print('nombre de usuario no valido')
        #     else: 
        #         break
        # con = Conexion(host, user, password_con, db)
        # usuario_existente = con.obtener_usuario(username)

        # if usuario_existente:
        #     print("nombre de usuario ya existe")
        #     seguir = input("¿Desea continuar? Si/No ")
        #     if seguir.lower() == "no":
        #         break
        #     else:
        #         continue

        while True:
            nombre = input('Ingrese nombre: ')
            apellido = input('Ingrese apellido: ')
            if nombre == '' or apellido == '':
                print("nombre y/o apellido no validos")
                continue
            elif nombre.isalpha() == False or apellido.isalpha() == False:
                print("nombre y/o apellido no validos")
                continue
            elif ' ' in nombre or ' ' in apellido:
                print("nombre y/o apellido no validos")
                continue
            else:
                break

        while True:
            correo = input('Ingrese correo: ')
            if not correo.endswith("@gmail.com"):
                print('Debe ingresar un correo válido, usando el formato "@gmail.com"')
                continue
            else:
                break

        while True:
            clave1 = getpass("Ingrese contraseña: ")
            clave2 = getpass("Vuelva a escribir la contraseña: ")
            if clave1 == '' or clave2 == '':
                print("Campo contraseña no puede estar vacio")
                continue
            if clave1 == clave2:
                password = clave1
                if ' ' in password:
                    print("La contraseña no puedecontener espacios")
                    continue
                if clave1.isalpha():
                    print("La contraseña debe contener al menos 1 numero")
                    continue
                if clave1.isdigit():
                    print("La contraseña debe contener al menos 1 letra")
                    continue
                if clave1.isalnum() == False:
                    print("La contraseña no puede contener simbolos")  
                    continue
                if len(clave1) < 6:
                    print("La contraseña debe ser igual o mayor a 6 caracteres")
                else:
                    break
            else:
                print("Las contraseñas no coinciden, reintente")
        

        os.system("cls")
        print("-------- TIPOS DE USUARIOS --------")
        print("     1.- Administrador")
        print("     2.- Usuario \n")    
        while True:
            try:
                tipo = input("Ingrese numero de opción: ")
                if tipo == '1':
                    tipo = "administrador"
                    break
                elif tipo == '2':
                    tipo = "usuario"
                    break
                else:
                    print("seleccione una opcion valida (1 o 2)")
                    continue
            except:
                print("Numero no valido")
                continue
        
        
        user = Usuario(nombre, apellido, correo, password=password)
       
        user.registrar_usuario()
        input('Presione una tecla para continuar')
        break

        
menu_login()