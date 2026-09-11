from cursos import Curso

class Teorico (Curso):
    def __init__(self, tipo_curso,codigo, nombre_curso, precio_base_est, cant_alumnos):
        super().__init__(tipo_curso,codigo, nombre_curso, precio_base_est, cant_alumnos)
        self.tipo_curso = 1


    def calcular_precio(self):
        if self.cant_alumnos > 50:
            return self.precio_base_est*0.9
        return self.precio_base_est
    