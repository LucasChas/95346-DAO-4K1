from abc import ABC, abstractmethod


class Vehiculo(ABC):
    def __init__(self,tipo,matricula, marca,modelo,costo_base_mant):
        self.tipo = tipo
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.costo_base_mant = costo_base_mant

    def __str__(self):
        return f"| Tipo: {self.tipo} | Matricula: {self.matricula} | Marca: {self.marca} | Modelo: {self.modelo} | Costo mantenimiento ${self.calcular_costo_mantenimiento()}"
    @abstractmethod
    def calcular_costo_mantenimiento(self):
        ...
    