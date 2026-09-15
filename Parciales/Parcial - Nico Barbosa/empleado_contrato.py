from empleado import Empleado

class Contrato(Empleado):
    def __init__(self, tipo, codigo, nombre, salario_base):
        super().__init__(tipo, codigo, nombre, salario_base)
        