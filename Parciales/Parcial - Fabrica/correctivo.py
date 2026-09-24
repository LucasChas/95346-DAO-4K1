from mantenimiento import Mantenimiento

class Correctivo(Mantenimiento):
    def __init__(self, tipo, fecha, operario, importe_repuestos,cantidad_horas_parada,importe_cobro_tecnico):
        super().__init__(tipo, fecha, operario, importe_repuestos)
        self.cantidad_horas_parada = cantidad_horas_parada
        self.importe_cobro_tecnico = importe_cobro_tecnico


    def __str__(self):
        return f"{super().__str__()} | Cantidad de horas parada: {self.cantidad_horas_parada} Hs. | Importe del tecnico: {self.importe_cobro_tecnico} | Gasto total: ${self.gasto_manteminiento()}"

    def gasto_manteminiento(self):
        return self.importe_repuestos + self.importe_cobro_tecnico

    