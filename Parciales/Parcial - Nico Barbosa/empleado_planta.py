from empleado import Empleado

class Planta(Empleado):
    def __init__(self, tipo, codigo, nombre, salario_base,años_antiguedad):
        super().__init__(tipo, codigo, nombre, salario_base)
        self.tipo = 1
        self.años_antiguedad = años_antiguedad
    #Empleados de planta: Reciben un bono adicional del 20% si cumplen más  de 5 años en la empresa.
    def calcular_salario(self):
        if self.años_antiguedad >= 5:
            return self.salario_base*1.20
        return self.salario_base

    