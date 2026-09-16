from vehiculo import Vehiculo

class Auto(Vehiculo):
    def __init__(self, tipo, matricula, marca, modelo, costo_base_mant,kilometraje):
        super().__init__(tipo, matricula, marca, modelo, costo_base_mant)

        self.kilometraje = kilometraje

    def __str__(self):
        return f"{super().__str__()} | Kilometraje: {self.kilometraje} Km. | "
    def calcular_costo_mantenimiento(self):
        if self.kilometraje > 100000:
            return self.costo_base_mant*1.10
        else: 
            return self.costo_base_mant
