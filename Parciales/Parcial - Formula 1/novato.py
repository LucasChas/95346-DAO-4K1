from piloto import Piloto

class Novato(Piloto):
    def __init__(self, numero, nombre, escuderia, sueldo_base, puntos,premio):
        super().__init__(3, numero, nombre, escuderia, sueldo_base, puntos)
        self.premio = premio
    
    def __str__(self):
        return super().__str__()
    
    def calcular_pago(self):
        total = self.sueldo_base + 500*self.puntos
        if self.premio == "si":
            return total*1.25
        else:
            return total

    