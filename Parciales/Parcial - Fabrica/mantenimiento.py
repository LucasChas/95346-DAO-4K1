from abc import ABC, abstractmethod

class Mantenimiento(ABC):
    def __init__(self,tipo,fecha,operario,importe_repuestos):
        self.tipo = tipo
        self.fecha = fecha
        self.operario = operario
        self.importe_repuestos = importe_repuestos

    def __str__(self):
        return f"| Tipo: {'Preventivo' if self.tipo == 1 else 'Correctivo'} | Fecha: {self.fecha} | Operario: {self.operario} | Importe de repuestos: {self.importe_repuestos}"

    @abstractmethod
    def gasto_manteminiento(self):
        pass

    
        