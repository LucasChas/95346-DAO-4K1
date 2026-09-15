from empleado import Empleado

class Contrato(Empleado):
    def __init__(self, tipo, codigo, nombre, salario_base, proyectos_completados):
        super().__init__(tipo, codigo, nombre, salario_base)

        self.tipo = 2
        self.proyectos_completados = proyectos_completados

    #Empleados por contrato: No reciben bonos por antigüedad, pero pueden recibir una prima mensual si han completado una cierta cantidad de proyectos (más de 3).
    #(no indica una prima mensual... le pongo el 15%)
    def calcular_salario(self):
        return self.salario_base*1.15
             