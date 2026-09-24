from piloto import Piloto

class Suplente(Piloto):
    def __init__(self,numero, nombre, escuderia, sueldo_base, puntos,carreras):
        super().__init__(2, numero, nombre, escuderia, sueldo_base, puntos)
        self.carreras = carreras

    def __str__(self):
        return super().__str__()
    
    def calcular_pago(self):
        return self.sueldo_base + 20000*self.carreras
    