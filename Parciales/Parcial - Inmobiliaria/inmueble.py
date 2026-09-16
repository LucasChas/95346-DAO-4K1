

from abc import ABC,abstractmethod

class Inmueble(ABC):
    def __init__(self,tipo,codigo,nombre_propietario, alquiler_base, superficie):
        self.tipo = tipo
        self.codigo = codigo
        self.nombre_propietario = nombre_propietario
        self.alquiler_base = alquiler_base
        self.superficie = superficie


    @abstractmethod
    def calcular_costo(self):
        pass

    def __str__(self):
        return F"| Codigo de inmueble: {self.codigo} | Propietario: {self.nombre_propietario} | Alquiler: ${self.calcular_costo()} | Superficie (m^2): {self.superficie}"