from piloto import Piloto

class Suplente(Piloto):
    def __init__(self, tipo, numero, nombre, escuderia, sueldo_base, puntos,carreras):
        super().__init__(tipo, numero, nombre, escuderia, sueldo_base, puntos)
        self.carreras = carreras

    def calcular_pago(self):
        return self.sueldo_base + 20000*self.carreras
    