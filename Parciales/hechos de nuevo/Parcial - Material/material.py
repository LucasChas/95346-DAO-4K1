from abc import ABC,abstractmethod

class Material(ABC):
    def __init__(self,tipo, codigo, titulo, autor, precio_base):
        self.tipo = tipo
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.precio_base = precio_base

    
    @abstractmethod
    def calcular_costo_mantenimiento(self):
        pass

    def __str__(self):
        return f"| Tipo: {"Libro" if self.tipo == 1 else ("Ebook" if self.tipo == 2 else "Revista")} | Codigo: {self.codigo} | Titulo: {self.titulo} | Autor: {self.autor} | Precio base: {self.precio_base} |"
        