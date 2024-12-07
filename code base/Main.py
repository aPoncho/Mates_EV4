import package.view.Login as login
from package.DTO.Ingreso import Ingreso
from package.DTO.Gasto import Gasto
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
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                id_user = input("Ingrese el ID del usuario: ")
                ultimos_gastos = Gasto.obtener_ultimos_gastos(id_user)
                if ultimos_gastos:
                    print("\n--- Últimos 5 Gastos ---")
                    for detalle in ultimos_gastos:
                        print(detalle)
                else:
                    print("No hay gastos disponibles.")

            elif opcion == "2":
                id_user = input("Ingrese el ID del usuario: ")
                promedio = Gasto.calcular_promedio_gastos(id_user)
                if promedio is not None:
                    print(f"El promedio de los gastos es: {promedio:.2f}")
                else:
                    print("No hay gastos registrados para este usuario.")

            elif opcion == "3":
                id_user = input("Ingrese el ID del usuario: ")
                resultado = Gasto.calcular_tendencia_gastos(id_user)
                if resultado:
                    pendiente, intercepto = resultado
                    print(f"Tendencia de gastos: Pendiente = {pendiente:.2f}, Intercepto = {intercepto:.2f}")

            elif opcion == "4":
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
            id_user = input("Ingrese el ID del usuario: ")
            ultimos_ingresos = Ingreso.obtener_ultimos_ingresos(id_user)
            if ultimos_ingresos:
                print("\n--- Últimos 5 ingresos ---")
                for detalle in ultimos_ingresos:
                    print(detalle)
            else:
                print("No hay ingresos disponibles.")

        elif opcion == "2":
            id_user = input("Ingrese el ID del usuario: ")
            promedio = Ingreso.calcular_promedio_ingresos(id_user)
            if promedio is not None:
                print(f"El promedio de los ingresos es: {promedio:.2f}")
            else:
                print("No hay ingresos registrados para este usuario.")

        elif opcion == "3":
            id_user = input("Ingrese el ID del usuario: ")
            resultado = Ingreso.calcular_tendencia_ingresos(id_user)
            if resultado:
                pendiente, intercepto = resultado
                print(f"Tendencia de ingresos: Pendiente = {pendiente:.2f}, Intercepto = {intercepto:.2f}")

        elif opcion == "4":
            print("Saliendo del menú. Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, intente nuevamente.")        

while True:
    user = login.menu_login()
    if user is not None:
        menu()
