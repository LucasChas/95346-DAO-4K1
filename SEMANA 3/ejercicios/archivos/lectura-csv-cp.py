# Lectura de un csv con códigos postales
# El archivo cp.csv contiene el listado de los códigos postales de tres provincias
# argentinas. En cada línea se encuentran, separados por un símbolo de punto
# y coma (;) los siguientes datos:
# • Provincia: representada por una letra mayúscula según el estándar ISO
# correspondiente.

# • Código: es un número entero de cuatro dígitos que identifica una locali-
# dad o varias localidades vecinas. Puede estar repetido.

# • Nombre: es el nombre de la localidad correspondiente a ese código.
# Se requiere leer todo el contenido del archivo y guardarlo en una lista que
# contenga un elemento por cada línea. En cada elemento debe almacenarse
# alguna estructura de datos que permita acceder individualmente a cada dato
# que conforma un codigo postal.
# Luego de la carga el programa debe permitir el ingreso de uno o más
# códigos numéricos y listar la provincia y nombre de todas las localidades
# asignadas a dichos códigos




def extraer_datos(nombre):
    archivo = open(nombre, "r", encoding="utf-8")
    lista= []
    sublista = []
    for i in archivo.readlines():
        sublista = (i[:-1].split(";"))
        lista.append(sublista)
    archivo.close()
    return lista


def buscar_codigo(lista, codigo):
    lista_encontrados = []
    for i in lista:
        if i[1] == codigo:
            lista_encontrados.append(i)
    return lista_encontrados

def main():
    lista = extraer_datos("cp.csv")
    codigo_a_buscar = input("Ingrese el codigo a buscar: ")
    while codigo_a_buscar:
        encontrado = buscar_codigo(lista,codigo_a_buscar)
        if encontrado:
            for i in encontrado:
                print(f"Registro encontrado.")
                print(f"Provicia: {i[0]}, Localidad: {i[2]}")
                print("-"*50)
        else:
            print("No se encontro ninguna localidad")
        codigo_a_buscar = input("Ingrese el codigo a buscar: ")

main()