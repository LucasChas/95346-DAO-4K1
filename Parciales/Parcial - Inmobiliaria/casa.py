

from inmueble import Inmueble

class Casa(Inmueble):
    def __init__(self, tipo, codigo, nombre_propietario, alquiler_base, superficie,cant_hab,tiene_pileta):
        super().__init__(tipo, codigo, nombre_propietario, alquiler_base, superficie)

        self.cant_hab = cant_hab
        self.tiene_pileta = tiene_pileta

    def __str__(self):
        return f"{super().__str__()} | Cantidad de habitaciones: {self.cant_hab} | ¿Tiene pileta? {'Si' if self.tiene_pileta == 1 else 'No'}"
    
    def calcular_costo(self):
        if self.tiene_pileta == 1:
            return (self.alquiler_base + 100000 + (self.cant_hab*30000))
        else:
            return (self.alquiler_base + (self.cant_hab*30000))
    