from abc import ABC, abstractmethod

class Carga(ABC):
    def __init__(self,contenido):
        self.contenido = contenido

    def __str__(self):
        return f"Contenido: {self.contenido}"

    @abstractmethod
    def peso(self):
        pass
    