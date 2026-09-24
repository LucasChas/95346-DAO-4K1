from carga import Carga

class Caja(Carga):
    def __init__(self, contenido,peso):
        super().__init__(contenido)
        self.peso_caja = peso

    def __str__(self):
        return f"{super().__str__()} | Peso de la caja: {self.peso_caja}"

    def peso(self):
        return self.peso_caja

    
