from material import Material

class Revista(Material):
    def __init__(self, codigo, titulo, autor, precio_base,origen):
        super().__init__(codigo, titulo, autor, precio_base)
        
        self.origen = origen


    def calcular_costo_mantenimiento(self):
        costo_x_ejemplar = 50
        org = "importada"
        if self.origen == org:
            return costo_x_ejemplar*1.20
        else: 
            return costo_x_ejemplar

    def __str__(self):
        return F"{super().__str__()} | Origen: {self.origen} | Costo mantenimimientos: ${self.calcular_costo_mantenimiento()}"
    
    