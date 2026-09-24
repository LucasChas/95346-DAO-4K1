from carga import Carga

class Packing(Carga):
    def __init__(self, contenido,peso_por_caja,cantidad,peso_estructura):
        super().__init__(contenido)
        self.peso_por_caja = peso_por_caja
        self.cantidad = cantidad
        self.peso_estructura = peso_estructura

    def __str__(self):
        pass

    def peso(self):
        return (self.peso_por_caja * self.cantidad) + self.peso_estructura

