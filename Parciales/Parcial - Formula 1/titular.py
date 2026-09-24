from piloto import Piloto

class Titular(Piloto):
    def __init__(self, tipo, numero, nombre, escuderia, sueldo_base, puntos,victorias):
        super().__init__(tipo, numero, nombre, escuderia, sueldo_base, puntos)
        self.victorias = victorias

    def calcular_pago(self):
        total = self.sueldo_base + 1000*self.puntos + 50000*self.victorias
        if self.victorias >= 5:
            return total*1.10
        else: 
            return total
    