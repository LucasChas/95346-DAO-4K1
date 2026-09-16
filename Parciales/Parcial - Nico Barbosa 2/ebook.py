from material import Material

class Ebook(Material):
    def __init__(self,codigo,titulo,autor,precio_base,ventas):
        super().__init__(2,codigo,titulo,autor,precio_base)
        self.ventas = ventas

    def calcular_precio_mantenimiento(self):
        # 5% sobre el valor de venta
        return self.ventas * 0.05
    