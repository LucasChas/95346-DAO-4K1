from carga import Carga

class Bidon(Carga):
    def __init__(self, contenido,capacidad,densidad):
        super().__init__(contenido)
        self.capacidad = capacidad
        self.densidad = densidad

    def __str__(self):
        return f"{super().__str__()} | Capacidad: {self.capacidad} | Densidad: {self.densidad} | Peso final: {self.peso()}"

    def peso(self):
        return self.capacidad * self.densidad