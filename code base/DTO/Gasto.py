class Gasto():
    def __init__(self, monto, fecha, descripcion, id = 'NO ID'):
        self.id = id
        self.monto = monto
        self.fecha = fecha
        self.descripcion = descripcion

    def resumen(self):
        return f'''Gasto: {self.descripcion}
ID: {self.id}
Fecha: {self.fecha}
Monto: {self.monto}'''
    
    