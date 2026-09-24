from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self,tipo,codigo,nombre,salario_base):
        self.tipo = tipo
        self.codigo = codigo
        self.nombre = nombre
        self.salario_base = salario_base


    def __str__(self):
        return f"| Tipo: {'Planta' if self.tipo == 1 else ('Contratado' if self.tipo == 2 else 'Vendedor')} | Codigo: {self.codigo} | Nombre: {self.nombre} | Salario base: ${self.salario_base}"

    @abstractmethod
    def calcular_salario(self):
        pass
        