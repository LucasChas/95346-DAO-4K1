from abc import ABC, abstractmethod

class Piloto(ABC):
    def __init__(self,tipo,numero,nombre,escuderia,sueldo_base,puntos):
       if puntos < 0:
            raise ValueError("La cantidad de puntos no puede ser negativa.")
       self.tipo = tipo
       self.numero = numero
       self.nombre = nombre
       self.escuderia = escuderia
       self.sueldo_base = sueldo_base
       self.puntos = puntos


    @abstractmethod
    def calcular_pago(self):
        pass
