CORAZON, PULMON, OTRAS = 1, 2, 3

class Paciente():
    def __init__(self,nombre, sintoma,habitual=False):
        if sintoma not in (CORAZON, PULMON, OTRAS):
            raise ValueError(f"Sintoma invalido: {sintoma}")

        self.nombre = nombre
        self.sintoma = sintoma
        self.habitual =  habitual

    def __str__(self):
        sintomas = {1: "corazon", 2: "pulmon", 3: "otras"}
        sintoma_str = sintomas.get(self.sintoma, "otras")
        return f"Nombre: {self.nombre} | Sintoma: {sintoma_str} | ¿Es habitual?: {'Si' if self.habitual else 'No'}"
    