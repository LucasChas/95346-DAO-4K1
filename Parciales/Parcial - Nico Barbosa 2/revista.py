from material import Material

class Revista(Material):
    def __init__(self, codigo, titulo, autor, precio_base,importacion):
        super().__init__(3, codigo, titulo, autor, precio_base)
        self.importacion = importacion

    def calcular_costo_mantenimiento(self):
        # $50 fijos + 20% de recargo si es importada ($60)
        costo = 50.0
        if self.importacion == "importada":
            costo += costo * 0.20
        return costo