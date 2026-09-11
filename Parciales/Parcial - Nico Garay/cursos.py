from abc import ABC, abstractmethod
class Curso(ABC):
    def __init__(self, tipo_curso,codigo, nombre_curso, precio_base_est, cant_alumnos):
        self.tipo_curso = int(tipo_curso)
        self.codigo = str(codigo)
        self.nombre_curso = str(nombre_curso)
        self.precio_base_est = float(precio_base_est)
        self.cant_alumnos = int(cant_alumnos)

    @abstractmethod
    def calcular_precio(self) -> float:
            ...

    def calcular_precio_total(self) -> float:
        return self.calcular_precio() * self.cant_alumnos
    def __str__(self):
        return (f"[{self.__class__.__name__}] {self.nombre_curso} | "
                f"Alumnos: {self.cant_alumnos} | "
                f"Precio final p/estudiante: ${self.calcular_precio():.2f} | "
                f"Total recaudado: ${self.calcular_precio_total():.2f}")


