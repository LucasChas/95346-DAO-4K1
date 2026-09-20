from maquina import Maquina

def main():
    nombre_archivo = "./data/mantenimientos.csv"
    maquina = Maquina(nombre_archivo)

    print("Listado de manteniminetos: ")
    print("-"*200)
    for mantenimiento in maquina.mantenimientos:
        print(mantenimiento)
        print("-"*200)
    print("\n")
    print("Estadisticas: ")
    print("-"*50)
    print(f"Cantidad de gasto total: ${maquina.suma_gastos()}")
    print("-"*50)

    print(f"Cantidad de mantenimientos caros: {maquina.cant_mant_caros()}")
    print("-"*50)

    print(f"Rotura mas larga: {maquina.rotura_mas_larga()}")
    print("-"*50)


if __name__ == "__main__":
    main()