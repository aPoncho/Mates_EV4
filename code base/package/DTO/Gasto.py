import package.DAO.CRUDGastos as Gastos
import numpy as np
import matplotlib.pyplot as plt

class Gasto():
    def __init__(self, monto, fecha, descripcion, id = 'NO ID'):
        self.id = id
        self.monto = monto
        self.fecha = fecha
        self.descripcion = descripcion

    def __str__(self):
        return f'\033[31m🡾🡾\033[0mID: {self.id} \nFECHA: {self.fecha} \nMONTO: {self.monto}\nDESCRIPCION: {self.descripcion}'

    def total_gastos(self, user):
        correo = user.email

        try:
            datos = Gastos.obtener_gastos(correo)
            total_gastos = 0

            for dato in datos:
                dato = Gasto(dato[0], dato[2], dato[3], dato[4])
                total_gastos += Gasto.monto
            
            return total_gastos
        
        except:
            print('error inesperado')
    @staticmethod
    def obtener_ultimos_gastos(id_user):
        gastos = Gastos.obtener_gastos(id_user)
        print(gastos)
        ultimos_gastos = gastos[:5]  
        detalles = []

        for i in ultimos_gastos:
            gasto = Gasto(i[2], i[3], i[4], i[0])
            detalle = f"ID: {gasto.id}, Monto: {gasto.monto}, Fecha: {gasto.fecha}, Descripción: {gasto.descripcion}"
            detalles.append(detalle)

        return detalles
    @staticmethod
    def calcular_promedio_gastos(id_user):
        gastos = Gastos.obtener_gastos(id_user)

        if not gastos: 
            print('no hay gastos relacionados') 
            return None

        total_monto = 0
        for gasto in gastos:
            total_monto += gasto[2]  

        promedio = total_monto / len(gastos)
        return promedio
    @staticmethod
    def calcular_tendencia_gastos(id_user):
        """
        Calcula y muestra una regresión lineal sobre los montos de los gastos de un usuario.

        :param id_user: ID del usuario para obtener sus gastos.
        :return: Una tupla con la pendiente y el intercepto de la línea de tendencia.
        """
        gastos = Gastos.obtener_gastos(id_user)

        if not gastos:
            print("No hay gastos registrados para este usuario.")
            return None

        # Obtener montos y generar índices como eje x (suponiendo que están en orden cronológico)
        montos = [gasto[0] for gasto in gastos]  # Se asume que el monto está en el índice 0
        x = np.arange(len(montos))  # Índices como eje x

        # Ajuste de regresión lineal
        coeficientes = np.polyfit(x, montos, 1)  # Regresión lineal (grado 1)
        pendiente, intercepto = coeficientes

        # Generar valores de la línea de tendencia
        tendencia = np.polyval(coeficientes, x)

        # Visualización
        plt.figure(figsize=(10, 6))
        plt.scatter(x, montos, color='blue', label='Montos')
        plt.plot(x, tendencia, color='red', label=f'Tendencia: y = {pendiente:.2f}x + {intercepto:.2f}')
        plt.title("Tendencia de los gastos")
        plt.xlabel("Número de gasto (índice)")
        plt.ylabel("Monto")
        plt.legend()
        plt.grid(True)
        plt.show()

        return pendiente, intercepto

    def ingresar(self, user_id):
        try:
            Gastos.ingresar_gasto(user_id, self.monto, self.fecha, self.descripcion)
        except Exception as e:
            input(e)
            