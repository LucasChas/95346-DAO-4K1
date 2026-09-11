from cursos import Curso

class Online(Curso):
    def __init__(self, tipo_curso, codigo,nombre_curso, precio_base_est, cant_alumnos, tutorias_personalizadas):
        super().__init__(tipo_curso, codigo,nombre_curso, precio_base_est, cant_alumnos)
        tipo_curso = 3
        self.tutorias_personalizadas = bool(tutorias_personalizadas)

    def calcular_precio(self):
        if self.tutorias_personalizadas:
            return self.precio_base_est*1.15
        return self.precio_base_est
    def __str__(self):
        tutorias = "Sí" if self.tutorias_personalizadas else "No"
        return f"{super().__str__()} | Tutorías: {tutorias}"
    
    