from sucursal import Sucursal

class Super(Sucursal):
    def __init__(self, tipo, numero, superficie, facturacion, es_mayorista):
        super().__init__(tipo, numero, superficie, facturacion)
        self.es_mayorista = es_mayorista

    def __str__(self):
        return f"{super().__str__()} | Tipo de comercio: {'Mayorista' if self.es_mayorista == 1 else 'Minorista'} | Resultado comercial: {self.resultado_comercial()} | Indice de rentabilidad: {self.indice_rentabilidad()} | "


    def resultado_comercial(self):
        return self.facturacion

    def indice_rentabilidad(self):
        return self.resultado_comercial() /self.superficie

    