
from empresa import Empresa

def main():
    nombre_archivo = "vehiculos.csv"
    empresa = Empresa(nombre_archivo)

    print(f"El costo de mantenimiento total es de: ${empresa.calcular_costo_total_matenimiento()}")
    print("-"*100)

    for vehiculo in empresa.vehiculos:
        print(vehiculo)
        print("-"*120)

    print(f"El vehiculo con el costo mas alto es de: \n {empresa.vehiculo_costo_mas_alto()}")
    print("-"*100)

    print(f"La cantidad de camionetas con mas de 1000Kg de capacidad de carga es de: {empresa.camionetas_mas_mil_kg()}")
    print("-"*100)

    print(f"La cantidad de motos de alta cilidrada (mas de 500cc.) es de: {empresa.motos_alta_cilidrada()}")

main()