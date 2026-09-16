from vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, tipo, matricula, marca, modelo, costo_base_mant, cilidrada):
        super().__init__(tipo, matricula, marca, modelo, costo_base_mant)
        self.cilindrada = cilidrada

    def __str__(self):
        return f"{super().__str__()} | Cilindrada: {self.cilindrada} cc. | "



    def calcular_costo_mantenimiento(self):
        if self.cilindrada > 500:
            return self.costo_base_mant*1.20
        else:
            return self.costo_base_mant