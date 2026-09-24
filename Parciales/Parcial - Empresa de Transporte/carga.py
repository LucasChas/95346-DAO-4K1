from abc import ABC,abstractmethod

class Carga(ABC):
    def __init__(self, contenido):
        self.contenido = contenido

    def __str__(self) -> str:
        return f"{self.contenido} (Peso: {self.peso():.2f} kg)"
    @abstractmethod
    def peso(self):
        pass