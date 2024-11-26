class Presupuesto():
    def __init__(self, ingreso, e_necesidades, e_deseos, e_ahorro, g_necesidades, g_deseos, g_ahorro,  id = 'NO ID' ):
        self.id = id
        self.ingreso = ingreso
        self.e_necesidades = e_necesidades
        self.e_deseos = e_deseos
        self.e_ahorro = e_ahorro
        self.g_necesidades = g_necesidades
        self.g_deseos = g_deseos
        self.g_ahorro = g_ahorro

    def total_estimados(self):
        estimados = self.e_necesidades + self.e_deseos + self.e_ahorro
        return estimados
    
    def total_gastos(self):
        gastos = self.g_necesidades + self.g_deseos + self.g_ahorro
        return gastos

    