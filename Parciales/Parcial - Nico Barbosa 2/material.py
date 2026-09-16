from abc import ABC,abstractmethod

class Material(ABC):
    def __init__(self, tipo, codigo, titulo, autor, precio_base):
        self.tipo = tipo
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.precio_base = precio_base
    @abstractmethod
    def calcular_precio_mantenimiento(self):
        pass