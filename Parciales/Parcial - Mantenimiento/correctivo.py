from mantenimiento import Mantenimiento

class Correctivo(Mantenimiento):
    def __init__(self, tipo_mantenimiento, fecha, operario, importe_repuesto,cantidad_horas_parada, importe_tecnico):
        super().__init__(tipo_mantenimiento, fecha, operario, importe_repuesto)
        self.cantidad_horas_parada = cantidad_horas_parada
        self.importe_tecnico = importe_tecnico

    def __str__(self):
        return f"{super().__str__()} | Cantidad de horas parada: {self.cantidad_horas_parada} hs | importe del tecnico: ${self.importe_tecnico} | Gasto total: ${self.gastos_mantenimiento()}"

    def gastos_mantenimiento(self):
        return self.importe_repuesto + self.importe_tecnico
