import csv
from caja import Caja
from camion import Camion
from bidon import Bidon
from packing import Packing


def cargar_cajas_desde_csv(ruta: str) -> list[Caja]:
    cajas = []
    with open(ruta, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            cajas.append(Caja(
                contenido=fila["producto"],
                peso_valor=float(fila["peso"])
            ))
    return cajas


def cargar_bidones_desde_csv(ruta: str) -> list[Bidon]:
    bidones = []
    with open(ruta, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            bidones.append(Bidon(
                contenido=fila["producto"],
                capacidad=float(fila["capacidad"]),
                densidad=float(fila["densidad"])
            ))
    return bidones


def cargar_packings_desde_csv(ruta: str) -> list[Packing]:
    packings = []
    with open(ruta, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            packings.append(Packing(
                contenido=fila["producto"],
                peso_por_caja=float(fila["peso"]),
                cantidad=int(fila["cantidad"]),
                peso_estructura=float(fila["estructura"])
            ))
    return packings


def main():
    # 1. Leer e instanciar todas las cargas de los archivos CSV
    todas_las_cargas = []
    todas_las_cargas.extend(cargar_cajas_desde_csv("data/cajas.csv"))
    todas_las_cargas.extend(cargar_bidones_desde_csv("data/bidones.csv"))
    todas_las_cargas.extend(cargar_packings_desde_csv("data/packing.csv"))

    print(f"Total de cargas leídas: {len(todas_las_cargas)}")

    # 2. Instanciar camión (por ejemplo, con capacidad de 300 kg)
    camion = Camion(patente="AF987XY", carga_maxima=300.0)

    # 3. Intentar subir las cargas respetando la carga máxima
    print("\n--- Iniciando proceso de carga ---")
    cargas_no_subidas = []
    for carga in todas_las_cargas:
        if not camion.subir_carga(carga):
            cargas_no_subidas.append(carga)

    # 4. Estado final del camión
    print(f"\n{camion}")
    print(f"¿Listo para salir?: {camion.listo_para_salir()}")
    print(f"Cargas que quedaron fuera por sobrepeso: {len(cargas_no_subidas)}")

    # 5. Listar lo que quedó cargado
    print("\nDetalle de cargas a bordo:")
    print(camion.cargas_en_orden())


if __name__ == "__main__":
    main()