from inmueble import Inmueble

class Departamento(Inmueble):
    def __init__(self, tipo, codigo, nombre_propietario, alquiler_base, superficie,expensas,piso):
        super().__init__(tipo, codigo, nombre_propietario, alquiler_base, superficie)
        self.expensas = expensas
        self.piso = piso

    def __str__(self):
        return f"{super().__str__()}( | Expensas (ya estan contempladas en el alquiler): {self.expensas} | Número de piso: {self.piso}"
    
    def calcular_costo(self):
        if self.piso < 3:
            return self.alquiler_base + self.expensas + 20000
        else:
            return self.alquiler_base + self.expensas