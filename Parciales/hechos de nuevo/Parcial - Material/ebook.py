from material import Material

class Ebook(Material):
    def __init__(self, codigo, titulo, autor, precio_base,valor_venta):
        super().__init__(2,codigo, titulo, autor, precio_base)
        self.valor_venta = valor_venta

    def calcular_costo_mantenimiento(self):
        return  (0.05*self.valor_venta)

    def __str__(self):
        return F"{super().__str__()} | Valor de venta: ${self.valor_venta} | Costo mantenimimientos: ${self.calcular_costo_mantenimiento()}"

    