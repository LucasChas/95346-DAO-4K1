from material import Material
import math
class Libro(Material):
    def __init__(self,codigo, titulo, autor, precio_base,dias_prestados):
        super().__init__(1,codigo,titulo,autor,precio_base)

        self.dias_prestados = dias_prestados

    def calcular_costo_mantenimiento(self):
        if self.dias_prestados == 0:
            return 0
        return math.ceil(self.dias_prestados / 30) * 100



    
