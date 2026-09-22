from material import Material

class Libro(Material):
    def __init__(self,codigo, titulo, autor, precio_base,dias_prestados):
        super().__init__(codigo, titulo, autor, precio_base)
        self.dias_prestados = dias_prestados

    def calcular_costo_mantenimiento(self):
        costo = 100
        return  (self.dias_prestados//30)*costo


    def __str__(self):
        return F"{super().__str__()} | Cantidad de dias prestados: {self.dias_prestados} | Costo mantenimimientos: ${self.calcular_costo_mantenimiento()}"