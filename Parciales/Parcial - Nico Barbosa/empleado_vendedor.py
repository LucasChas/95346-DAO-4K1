from empleado import Empleado

class Vendedor(Empleado):
    def __init__(self, tipo, codigo, nombre, salario_base,ventas):
        super().__init__(tipo, codigo, nombre, salario_base)
        self.tipo = 3
        self.ventas = ventas
    #Vendedores: Reciben una comisión del 5% sobre el total de sus ventas.
    def calcular_salario(self):
        return (self.salario_base + (self.ventas*0.05))
    