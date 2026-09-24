from empresa import Empresa

def main():
    empresa = Empresa("empleados.csv")
    print("-"*200)

    for empleado in empresa.empleados:
        print(empleado)
        print("-"*200)

    print("\n")

    print(f"Total de salarios por tipo: {empresa.salario_total_por_tipo()}")
    print("-"*200)
    print(f"Total a pagar en salarios: ${empresa.calcular_salario_total()}")
    print("-"*200)
    print(f"Nombre del empleado con salario mas bajo: {empresa.empleado_salario_mas_bajo()}")
    print("-"*200)
    print(f"Cantidad de empleados con bonificacion de antiguedad: {empresa.empleados_mas_5_años_antiguedad()}")
    print("-"*200)
    print(f"Cantidad de empleados que reciben prima por contrato: {empresa.empleados_que_reciben_prima()}")
    print("-"*200)

if __name__ == "__main__":
    main()