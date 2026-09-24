from piloto import Piloto

class Novato(Piloto):
    def __init__(self, tipo, numero, nombre, escuderia, sueldo_base, puntos,premio):
        super().__init__(tipo, numero, nombre, escuderia, sueldo_base, puntos)