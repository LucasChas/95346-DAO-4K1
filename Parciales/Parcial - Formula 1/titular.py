from piloto import Piloto

class Titular(Piloto):
    def __init__(self, numero, nombre, escuderia, sueldo_base, puntos,victorias):
        super().__init__(1, numero, nombre, escuderia, sueldo_base, puntos)
        self.victorias = victorias

    def __str__(self):
        return super().__str__()
    
    def calcular_pago(self):
        total = self.sueldo_base + 1000*self.puntos + 50000*self.victorias
        if self.victorias >= 5:
            return total*1.10
        else: 
            return total
    