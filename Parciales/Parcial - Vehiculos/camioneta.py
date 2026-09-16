from vehiculo import Vehiculo

class Camioneta(Vehiculo):
    def __init__(self, tipo, matricula, marca, modelo, costo_base_mant,capacidad_carga):
        super().__init__(tipo, matricula, marca, modelo, costo_base_mant)
        self.capacidad_carga = capacidad_carga


    def __str__(self):
        return f"{super().__str__()} | Capacidad de carga: {self.capacidad_carga} Kg. | "


    def calcular_costo_mantenimiento(self):
        if self.capacidad_carga > 1000:
            return self.costo_base_mant*1.15
        else:
            return self.costo_base_mant
