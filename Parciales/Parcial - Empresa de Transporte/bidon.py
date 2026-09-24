from carga import Carga

class Bidon(Carga):
    def __init__(self, contenido, capacidad, densidad):
        super().__init__(contenido)
        self.capacidad = capacidad
        self.densidad = densidad

    def __str__(self) -> str:
        return (f"Bidón de {self.contenido} | Capacidad: {self.capacidad} L "
                f"(Densidad: {self.densidad}) | Peso: {self.peso():.2f} kg")

    def peso(self):
        return self.capacidad*self.densidad 

    