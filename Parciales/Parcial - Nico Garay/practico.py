
from cursos import Curso

class Practico(Curso):
    def __init__(self, tipo_curso, codigo,nombre_curso, precio_base_est, cant_alumnos, practicas_laboratorio):
        super().__init__(tipo_curso, codigo,nombre_curso, precio_base_est, cant_alumnos)
        self.tipo_curso = 2
        self.practicas_laboratorio = int(practicas_laboratorio)

    def calcular_precio(self):
        return self.precio_base_est + 500 * self.practicas_laboratorio
    def __str__(self):
        return f"{super().__str__()} | Prácticas Lab: {self.practicas_laboratorio}"