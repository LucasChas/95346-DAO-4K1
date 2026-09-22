from biblioteca import Biblioteca

def main():
    biblioteca = Biblioteca("material.csv")
    print("-"*50)
    print(f"Promedio entero de los precios bases: ${biblioteca.calcular_promedio_precios_base()}")
    print("-"*50)
    mayor_costo = biblioteca.obtener_material_mayor_costo_mantenimiento()
    print(f"Material con el mayor costo de mantenimiento: {mayor_costo.titulo} con un costo de: ${mayor_costo.calcular_costo_mantenimiento()}")
    print("-"*50)
    print(f"El total de costo de mantenimiento es: {biblioteca.calcular_suma_costo_mantenimiento()}")
    print("-"*50)
    print(f"La cantidad de Libros fisicos que se prestaron mas de 30 dias es de: {biblioteca.contar_libros_mas_30_dias()}")
    print("-"*50)
    print(F"La cantidad de revistas importadas es de: {biblioteca.contar_revistas_importadas()}")
    print("-"*50)
    print(F"La cantidad de materiales por tipo es: {biblioteca.cantidad_por_tipo()}")
    print("-"*50)


if __name__ =="__main__":
    main()