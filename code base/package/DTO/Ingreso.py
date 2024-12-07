import package.DAO.CRUDIngresos as Ingresos 
import numpy as np
import matplotlib.pyplot as plt

class Ingreso():
    def __init__(self, monto, fecha, descripcion, id = 'NO ID'):
        self.id = id
        self.monto = monto
        self.fecha = fecha
        self.descripcion = descripcion

    def __str__(self):
        return f'\033[32m🡽🡽\033[0mID: {self.id} \nFECHA: {self.fecha} \nMONTO: {self.monto}\nDESCRIPCION: {self.descripcion}'
    @staticmethod
    def obtener_ultimos_ingresos(id_user):
        ingresos = Ingresos.obtener_ingresos(id_user)
        ultimos_ingresos = ingresos[:-5]  
        detalles = []

        for i in ultimos_ingresos:
            ingreso = Ingreso(i[0], i[2], i[3], i[4])
            detalle = f"ID: {ingreso.id}, Monto: {ingreso.monto}, Fecha: {ingreso.fecha}, Descripción: {ingreso.descripcion}"
            detalles.append(detalle)

        return detalles
    @staticmethod
    def calcular_promedio_ingresos(id_user):
        ingresos = Ingresos.obtener_ingresos(id_user)

        if not ingresos: 
            print('no hay ingresos relacionados') 
            return None

        total_monto = 0
        for ingreso in ingresos:
            total_monto += ingreso[2]  

        promedio = total_monto / len(ingresos)
        return promedio
    @staticmethod
    def calcular_tendencia_ingresos(id_user):
        """
        Calcula y muestra una regresión lineal sobre los montos de los ingresos de un usuario.

        :param id_user: ID del usuario para obtener sus ingresos.
        :return: Una tupla con la pendiente y el intercepto de la línea de tendencia.
        """
        ingresos = Ingresos.obtener_ingresos(id_user)

        if not ingresos:
            print("No hay ingresos registrados para este usuario.")
            return None

        # Obtener montos y generar índices como eje x (suponiendo que están en orden cronológico)
        montos = [ingreso[0] for ingreso in ingresos]  # Se asume que el monto está en el índice 0
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
        plt.title("Tendencia de los ingresos")
        plt.xlabel("Número de ingreso (índice)")
        plt.ylabel("Monto")
        plt.legend()
        plt.grid(True)
        plt.show()

        return pendiente, intercepto
    
    def ingresar(self, user_id):
        try:
            Ingresos.ingresar_ingreso(user_id, self.monto, self.fecha, self.descripcion)
        except Exception as e:
            input(e)