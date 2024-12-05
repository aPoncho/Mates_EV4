class Ingreso():
    def __init__(self, monto, fecha, descripcion, id = 'NO ID'):
        self.id = id
        self.monto = monto
        self.fecha = fecha
        self.descripcion = descripcion

    def __str__(self):
        return f'\033[32m🡽🡽\033[0mID: {self.id} \nFECHA: {self.fecha} \nMONTO: {self.monto}\nDESCRIPCION: {self.descripcion}'

   