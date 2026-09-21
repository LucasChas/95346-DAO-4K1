from empresa import Empresa

def main():
    nombre_archivo = "sucursales.csv"
    empresa = Empresa(nombre_archivo)
    print(" - Sistema de sucursales - ")
    print("-"*200)
    for emp in empresa.sucursales:
        print(emp)
        print("-"*200)
    
    print(f"Ganancias totales: ${empresa.suma_ganancias()}")
    print(f"Cantidad de locales no rentables: {empresa.cantidad_locales_no_rentables()}")
    print(f"Local más rentable: {empresa.local_mas_rentable()}")




if __name__ =="__main__":
    main()