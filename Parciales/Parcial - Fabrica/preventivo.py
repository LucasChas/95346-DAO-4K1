from mantenimiento import Mantenimiento

class Preventivo(Mantenimiento):
    def __init__(self, tipo, fecha, operario, importe_repuestos,resultado_mantenimiento, importe_insumos):
        super().__init__(tipo, fecha, operario, importe_repuestos)
        self.resultado_mantenimiento = resultado_mantenimiento
        self.importe_insumos = importe_insumos

    def __str__(self):
        return f"{super().__str__()} | Resultado del mantenimiento: {'funciona correctamente' if self.resultado_mantenimiento == 1 else ('Revisión tecnica recomendada' if self.resultado_mantenimiento == 2 else 'Rotura')} | Importe de insumos: ${self.importe_insumos} | Gasto total: ${self.gasto_manteminiento()} |"

    def gasto_manteminiento(self):
        return self.importe_repuestos + self.importe_insumos
    
