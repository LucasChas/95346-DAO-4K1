from carga import Carga

class Packing(Carga):
    def __init__(self, contenido,peso_por_caja,cantidad,peso_estructura):
        super().__init__(contenido)
        self.peso_por_caja = peso_por_caja
        self.cantidad = cantidad
        self.peso_estructura = peso_estructura

    def __str__(self):
        return f"{super().__str__()} | Peso por caja: {self.peso_por_caja} | Cantidad de cajas: {self.cantidad} | Peso de la estructura: {self.peso_estructura} | Peso final: {self.peso()}"

    def peso(self):
        return (self.peso_por_caja*self.cantidad) + self.peso_estructura

    