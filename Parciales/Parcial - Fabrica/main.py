from maquina import Maquina

def main():
    print("- Sistema de Fabrica -")
    print("-"*150)
    maquina = Maquina("mantenimientos.csv")

    for mantenimiento in maquina.mantenimientos:
        print(mantenimiento)
        print("-"*150)

    print(f"Total de gastos por los mantenimientos efectuados: ${maquina.suma_gastos()}")
    print("-"*150)
    print(f"Cantidad de mantenimientos caros: {maquina.cantidad_mant_caros()}")
    print("-"*150)
    print(f"Rotura más larga: {maquina.rotura_mas_larga()}")


if __name__ == "__main__":
    main()