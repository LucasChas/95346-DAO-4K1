from material import Material

class Libro(Material):
    def __init__(self ,codigo, titulo, autor, precio_base,dias_prestados):
        super().__init__(1,codigo,titulo,autor,precio_base)

        self.dias_prestados = dias_prestados

    def calcular_costo_mantenimiento(self):
        # $100 por cada bloque completo de 30 días prestados
        return (self.dias_prestados // 30) * 100



    
