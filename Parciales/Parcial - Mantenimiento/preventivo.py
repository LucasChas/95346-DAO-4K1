from mantenimiento import Mantenimiento

class Preventivo(Mantenimiento):
    def __init__(self, tipo_mantenimiento, fecha, operario, importe_repuesto,resultado, importe_insumos):
        super().__init__(tipo_mantenimiento, fecha, operario, importe_repuesto)

        self.resultado = resultado
        self.importe_insumos = importe_insumos

    def __str__(self):
        return f"{super().__str__()} | Resultado: {'Funciona correctamente (1)' if self.resultado == 1 else ('Recomienda revision (2)' if self.resultado == 2 else 'Detecto rotura (3)') } | Importe de insumos: ${self.importe_insumos} | Gasto total: ${self.gastos_mantenimiento()}"

    def gastos_mantenimiento(self):
        return self.importe_repuesto + self.importe_insumos
    
    