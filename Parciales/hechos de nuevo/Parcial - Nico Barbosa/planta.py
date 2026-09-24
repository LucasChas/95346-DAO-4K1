from empleado import Empleado

class Planta(Empleado):
    def __init__(self, tipo, codigo, nombre, salario_base, años_antiguedad):
        super().__init__(tipo,codigo, nombre, salario_base)
        self.años_antiguedad = años_antiguedad

    def __str__(self):
        return f"{super().__str__() } | Años de antigüedad: {self.años_antiguedad} | Salario final: ${self.calcular_salario()}"

    # Reciben un bono adicional del 20% si cumplen más de 5 años en la empresa.
    def calcular_salario(self):
        bono = 0.2
        if self.años_antiguedad > 5:
            return self.salario_base + self.salario_base*bono
        else:
            return self.salario_base

    