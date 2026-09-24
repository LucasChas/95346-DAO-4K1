from ebook import Ebook
from libro import Libro
from revista import Revista
from biblioteca import Biblioteca

def main():
    nombre_archivo = "material.csv"
    biblioteca = Biblioteca(nombre_archivo)

    print("Metricas:")
    print(f"Promedio entero de los precios base: {biblioteca.calcular_promedio_precios_base()}")
    print("-"*100)
    mayor_costo = biblioteca.obtener_material_mayor_costo_mantenimiento()
    print(f"Material con el mayor costo de mantenimiento: {mayor_costo.titulo} con un costo de: ${mayor_costo.calcular_costo_mantenimiento()}")

    print("-"*100)

    print(f"El total de costo de mantenimiento es de: ${biblioteca.calcular_suma_costo_mantenimiento()}")
    print("-"*100)

    print(f"La cantidad de libros con mas de 30 dias de prestamo es de: {biblioteca.contar_libros_mas_30_dias()}")
    print("-"*100)

    print(f"La cantidad de revistas importadas es de: {biblioteca.contar_revistas_importadas()}")
    print("-"*100)

    print(f"Diccionario con materiales por tipo: {biblioteca.cantidad_por_tipo()}")

main()