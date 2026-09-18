
from abc import ABC,abstractmethod
EFECTIVO, TARJETA = 1, 2
class Atencion(ABC):
    def __init__(self,codigo,tipoDeCobro):
        if tipoDeCobro not in (EFECTIVO, TARJETA):
            raise ValueError(f"Tipo de cobro invalido: {tipoDeCobro}")
        self.codigo = codigo
        self.tipoDeCobro = tipoDeCobro


    def __str__(self):
        return f"Codigo: {self.codigo} | Tipo de cobro: {'efectivo' if self.tipoDeCobro == 1 else 'tarjeta de credito' }"

    @abstractmethod
    def importeACobrar():
        pass

class AtencionMedica(Atencion):
    def __init__(self, codigo, tipoDeCobro, paciente, importe):
        super().__init__(codigo, tipoDeCobro)
        self.paciente = paciente
        self.importe = importe

    def esPacienteHabitual(self):
        return bool(self.paciente.habitual)

    
    def __str__(self):
        return f"Atencion Medica {self.codigo} | Paciente: {self.paciente.nombre} | Importe a cobrar: ${self.importeACobrar():.2f}"

    def importeACobrar(self):
        total = self.importe
        if self.paciente.habitual:
            total *= 0.75
        if self.tipoDeCobro == TARJETA:
            total *= 1.20
        elif self.tipoDeCobro == EFECTIVO:    # Efectivo (-10%)
            total *= 0.90
        return total



class AtencionFarmacia(Atencion):
    def __init__(self, codigo, tipoDeCobro,importeTotal,descuento):
        super().__init__(codigo, tipoDeCobro)
        self.importeTotal = importeTotal
        self.descuento = descuento

    def __str__(self):
        return f"Atencion Farmacia {self.codigo} | Importe a cobrar: ${self.importeACobrar():.2f}"

    def importeACobrar(self):
        total = self.importeTotal - self.descuento
        if self.tipoDeCobro == TARJETA:
            total *= 1.30

        elif self.tipoDeCobro == EFECTIVO:
            total *= 0.95
        return total
    
        

        