from carga import Carga

class Camion():
    # Estados posibles según el enunciado
    ESTADO_DISPONIBLE = "disponible"
    ESTADO_REPARACION = "en reparacion"
    ESTADO_EN_VIAJE = "en viaje"

    def __init__(self, patente: str, carga_maxima: float):
        self.patente = patente
        self.carga_maxima = carga_maxima
        self.estado = self.ESTADO_DISPONIBLE
        self.cargas: list[Carga] = []

    def cantidad_cargas(self) -> int:
        return len(self.cargas)

    def peso_cargas(self) -> float:
        return sum(c.peso() for c in self.cargas)

    def subir_carga(self, carga: Carga) -> bool:
        """
        Sube una carga si el camión está disponible
        y no satura su carga máxima.
        """
        if self.estado != self.ESTADO_DISPONIBLE:
            print(f"[{self.patente}] No se puede cargar: el camión está '{self.estado}'.")
            return False

        if self.peso_cargas() + carga.peso() > self.carga_maxima:
            print(f"[{self.patente}] No se puede cargar: supera la carga máxima permitida.")
            return False

        self.cargas.append(carga)
        return True

    def bajar_carga(self, carga: Carga) -> bool:
        """
        Baja una carga si el camión está disponible y la carga está en él.
        """
        if self.estado != self.ESTADO_DISPONIBLE:
            print(f"[{self.patente}] No se puede descargar: el camión está '{self.estado}'.")
            return False

        if carga in self.cargas:
            self.cargas.remove(carga)
            return True

        print(f"[{self.patente}] La carga indicada no se encuentra en el camión.")
        return False

    # Transiciones de estado
    def a_reparacion(self) -> None:
        if self.estado == self.ESTADO_EN_VIAJE:
            print(f"[{self.patente}] No puede entrar a reparación mientras está de viaje.")
            return
        self.estado = self.ESTADO_REPARACION

    def sale_reparado(self) -> None:
        if self.estado == self.ESTADO_REPARACION:
            self.estado = self.ESTADO_DISPONIBLE
        else:
            print(f"[{self.patente}] El camión no estaba en reparación.")

    def en_viaje(self) -> None:
        if self.estado == self.ESTADO_DISPONIBLE:
            self.estado = self.ESTADO_EN_VIAJE
        else:
            print(f"[{self.patente}] No puede viajar si no está disponible.")

    def de_regreso(self) -> None:
        if self.estado == self.ESTADO_EN_VIAJE:
            self.estado = self.ESTADO_DISPONIBLE
        else:
            print(f"[{self.patente}] El camión no estaba de viaje.")

    def listo_para_salir(self) -> bool:
        """
        Listo si está disponible y su carga total es al menos el 75% de su carga máxima.
        """
        return (self.estado == self.ESTADO_DISPONIBLE and
                self.peso_cargas() >= 0.75 * self.carga_maxima)

    def cargas_en_orden(self) -> str:
        """Retorna el listado de cargas contenidas para mostrar en pantalla."""
        if not self.cargas:
            return "Sin cargas a bordo."
        return "\n".join(f" - {c}" for c in self.cargas)

    def __str__(self) -> str:
        return (f"Camión [{self.patente}] | Estado: {self.estado} | "
                f"Carga actual: {self.peso_cargas():.2f} / {self.carga_maxima:.2f} kg "
                f"({self.cantidad_cargas()} bultos)")