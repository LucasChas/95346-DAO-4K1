from abc import ABC, abstractmethod

class Mantenimiento(ABC):
    def __init__(self, tipo_mantenimiento,fecha,operario, importe_repuesto):
        self.tipo_mantenimiento = tipo_mantenimiento
        self.fecha = fecha
        self.operario = operario
        self.importe_repuesto = importe_repuesto

    def __str__(self):
        return f" Tipo de mantenimiento: {'Preventivo' if self.tipo_mantenimiento == 1 else 'Correctivo'}  | fecha: {self.fecha} | Operario: {self.operario} | Importe: ${self.importe_repuesto}"

    @abstractmethod
    def gastos_mantenimiento(self):
        pass