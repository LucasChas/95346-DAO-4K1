from empleado import Empleado

class Contratado(Empleado):
    def __init__(self, tipo, codigo, nombre, salario_base,proyectos_completados):
        super().__init__(tipo, codigo, nombre, salario_base)
        self.proyectos_completados = proyectos_completados

    def __str__(self):
        return f"{super().__str__() } | Cantidad de proyectos completados: {self.proyectos_completados} | Salario final: ${self.calcular_salario()}"

    def calcular_salario(self):
        prima = 1.15 #No lo especifica el ejercicio (voy a poner 15% mas)

        if self.proyectos_completados > 3:
            return self.salario_base*prima
        else:
            return self.salario_base

    