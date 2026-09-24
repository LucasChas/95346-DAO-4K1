from carga import Carga

class Caja(Carga):
    def __init__(self, contenido,peso_valor):
        super().__init__(contenido)

    def __str__(self) -> str:
        return f"Caja suelta: {self.contenido} | Peso: {self.peso_valor():.2f} kg"

    def peso(self):
        return self.peso_valor
    