from inmobiliaria import Inmobiliaria

def main():
    nombre_archivo = "inmuebles.csv"
    inmobiliaria = Inmobiliaria(nombre_archivo)
    print("Inmuebles registrados: ")
    for i in inmobiliaria.inmuebles:
        print(i)
        print("-"*200)

    print("Estadisticas")
    print(f"Importe total por los alquileres: ${inmobiliaria.suma_alquileres()}")
    print(f"Cantidad de casas premium: {inmobiliaria.casas_premium()}")
    print(f"El propietario con alquiler mas bajo es: {inmobiliaria.propietario_mas_bajo()}")

main()