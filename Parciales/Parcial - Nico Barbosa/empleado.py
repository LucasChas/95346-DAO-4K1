
from abc import ABC,abstractmethod
class Empleado(ABC):
    def __init__(self,tipo,codigo,nombre,salario_base):
        self.tipo = tipo
        self.codigo = codigo
        self.nombre = nombre
        self.salario_base = salario_base

    def __str__(self):
        return f" | Codigo de empleado: {self.codigo} | Nombre: {self.nombre} "
    @abstractmethod
    def calcular_salario(self):
        ...


    
