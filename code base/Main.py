import package.view.Login as login
from package.DTO.Ingreso import Ingreso
from package.DTO.Gasto import Gasto
from datetime import datetime
import os



def menu():
    while True:
        os.system("cls")
        print("\n--- Menú de Gastos ---")
        print("1. Gastos")
        print("2. Ingresos")
        print("3. en construccion")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_gasto()

        elif opcion == "2":
            menu_ingreso()
        
        elif opcion == '3':
            input("en construccion")

        elif opcion == '4':
            break

        else:
            input("opcion no valida")

def menu_gasto():
        while True:
            os.system("cls")
            print("\n--- Menú de Gastos ---")
            print("1. Mostrar los últimos 5 gastos")
            print("2. Calcular el promedio de los gastos")
            print("3. Mostrar tendencia de los gastos")
            print("4. Ingresar gasto")
            print("5. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                ultimos_gastos = Gasto.obtener_ultimos_gastos(user.id)
                if ultimos_gastos:
                    print("\n--- Últimos 5 Gastos ---")
                    for detalle in ultimos_gastos:
                        print(detalle)
                    input()    
                else:
                    print("No hay gastos disponibles.")
                    input()

            elif opcion == "2":
                promedio = Gasto.calcular_promedio_gastos(user.id)
                if promedio is not None:
                    print(f"El promedio de los gastos es: {promedio:.2f}")
                    input()
                else:
                    print("No hay gastos registrados para este usuario.")
                    input()

            elif opcion == "3":
                resultado = Gasto.calcular_tendencia_gastos(user.id)
                if resultado:
                    pendiente, intercepto = resultado
                    print(f"Tendencia de gastos: Pendiente = {pendiente:.2f}, Intercepto = {intercepto:.2f}")
                
            elif opcion == '4':
                while True:
                    try:
                        monto = int(input("Ingrese monto: "))
                        break
                    except ValueError:
                        print("valor invalido")
                        continue
                    
                descripcion = input("Ingrese descripcion: ")
                while True:
                    fecha = input("Ingrese una fecha en formato YYYY-MM-DD: ")
                    try:
                        anio, mes, dia = map(int, fecha.split('-'))
                        if 1 <= mes <= 12 and 1 <= dia <= 31:
                            fecha_obj = datetime.strptime(fecha, "%Y-%m-%d")
                            break
                        else:
                            print("Fecha inválida. Asegúrese de usar un formato correcto.")
                            continue
                    except ValueError:
                        print("Entrada inválida. Por favor, use el formato YYYY-MM-DD.")
                data = Gasto(monto, fecha_obj, descripcion)
                data.ingresar(user.id)

            elif opcion == "5":
                print("Saliendo del menú. Hasta luego!")
                break

            else:
                print("Opción no válida. Por favor, intente nuevamente.")      

def menu_ingreso():
    while True:
        os.system("cls")
        print("\n--- Menú de ingresos ---")
        print("1. Mostrar los últimos 5 ingresos")
        print("2. Calcular el promedio de los ingresos")
        print("3. Mostrar tendencia de los ingresos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ultimos_ingresos = Ingreso.obtener_ultimos_ingresos(user.id)
            if ultimos_ingresos:
                print("\n--- Últimos 5 ingresos ---")
                for detalle in ultimos_ingresos:
                    print(detalle)
            else:
                print("No hay ingresos disponibles.")

        elif opcion == "2":
            promedio = Ingreso.calcular_promedio_ingresos(user.id)
            if promedio is not None:
                print(f"El promedio de los ingresos es: {promedio:.2f}")
            else:
                print("No hay ingresos registrados para este usuario.")

        elif opcion == "3":
            resultado = Ingreso.calcular_tendencia_ingresos(user.id)
            if resultado:
                pendiente, intercepto = resultado
                print(f"Tendencia de ingresos: Pendiente = {pendiente:.2f}, Intercepto = {intercepto:.2f}")

        elif opcion == "4":
            print("Saliendo del menú. Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, intente nuevamente.")        

while True:
    global user
    user = login.menu_login()
    if user is not None:
        menu()
