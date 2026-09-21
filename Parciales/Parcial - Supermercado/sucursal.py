from abc import ABC, abstractmethod

class Sucursal(ABC):
    def __init__(self,tipo,numero,superficie,facturacion):
        self.tipo = tipo
        self.numero = numero
        self.superficie = superficie
        self.facturacion = facturacion


    def __str__(self):
        return f"| Tipo: { 'Hipermercado' if self.tipo == 1 else ( 'Supermercado' if self.tipo == 2 else 'Minimercado')} | Número: {self.numero} | Superficie: {self.superficie} m^2 | Facturación: {self.facturacion}"

    @abstractmethod
    def resultado_comercial(self):
        pass

    @abstractmethod
    def indice_rentabilidad(self):
        pass