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

    def __str__(self):
        return f" | Tipo: {'Titular' if self.tipo == 1 else ('Suplente' if self.tipo == 2 else 'Novato')} | Número: {self.numero} | Nombre: {self.nombre} |Escuderia: {self.escuderia} | Cantidad de puntos {self.puntos} | Sueldo: ${self.calcular_pago()} |"
    
    @abstractmethod
    def calcular_pago(self):
        pass
