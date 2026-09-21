from sucursal import Sucursal


class Mini(Sucursal):
    def __init__(self, tipo, numero, superficie, facturacion, importe):
        super().__init__(tipo, numero, superficie, facturacion)
        self.importe = importe

    def __str__(self):
        return f"{super().__str__()} | Importe del alquiler: ${self.importe} | Resultado comercial: {self.resultado_comercial()} | Indice de rentabilidad: {self.indice_rentabilidad()} |"

    def resultado_comercial(self):
        return self.facturacion - self.importe

    def indice_rentabilidad(self):
        return self.resultado_comercial() / self.superficie
    
    