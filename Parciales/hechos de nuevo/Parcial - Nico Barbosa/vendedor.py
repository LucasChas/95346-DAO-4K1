from empleado import Empleado

class Vendedor(Empleado):
    def __init__(self, tipo, codigo, nombre, salario_base, total_ventas):
        super().__init__(tipo, codigo, nombre, salario_base)
        self.total_ventas = total_ventas

    def __str__(self):
        return f"{super().__str__() } | TotaL de ventas: {self.total_ventas} | Salario final: ${self.calcular_salario()}"

    def calcular_salario(self):
        return  self.salario_base + 0.05*self.total_ventas
