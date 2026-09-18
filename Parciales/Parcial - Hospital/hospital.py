from atencion import Atencion, AtencionFarmacia, AtencionMedica
class Hospital:
    def __init__(self, razonSocial, atencionesRealizadas=None):
        self.razonSocial = razonSocial
        self.atencionesRealizadas = atencionesRealizadas if atencionesRealizadas is not None else []

    def addAtencion(self, atencion):
        self.atencionesRealizadas.append(atencion)

    def atencionesMedicas(self):
        return [a for a in self.atencionesRealizadas if isinstance(a, AtencionMedica)]

    def importe_total_atencion_consulta(self):
        return sum(a.importe for a in self.atencionesMedicas())

    def importe_promedio_atenciones(self, minimo, maximo):
        medicas = self.atencionesMedicas()
        en_rango = [a.importeACobrar() for a in medicas if minimo <= a.importeACobrar() <= maximo]
        if not en_rango:
            return 0.0
        return sum(en_rango) / len(en_rango)

    def codigo_primera_atencion_habitual(self):
        for a in self.atencionesMedicas():
            if a.paciente.habitual:
                return a.codigo
        return 0

    def __str__(self):
        atenciones = "\n".join(str(a) for a in self.atencionesRealizadas)
        return f"Hospital: {self.razonSocial}\nAtenciones:\n{atenciones}"


        