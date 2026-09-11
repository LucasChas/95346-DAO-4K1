# Padrón de personas 
# El archivo personas.csv contiene un padrón de personas a razón de una persona por línea y en 
# cada una separadas con comas el documento, nombre, apellido y edad. Desarrollar un programa 
# en python que lea el archivo y guarde todo su contenido en un diccionario indexado por 
# documento. Luego el programa debe ofrecer un menú con las siguientes opciones: 
# • Búsqueda por documento: que solicite un documento y si lo encuentra muestre todos los datos 
# de la persona encontrada y un mensaje adecuado si no la encuentra. 
# • Búsqueda por apellido: que solicite un apellido y muestre por pantalla todos los datos de todas 
# las personas cuyo apellido sea igual al ingresado. 
# • Mostrar el promedio de edades de todos. 

def leer_padron(nombre):
    padron = {}
    with open(nombre, "r", encoding="utf-8") as archivo:
        for i in archivo:
            linea = i.strip()
            if linea:
                partes = linea.split(",")
                dni = int(partes[0])
                padron[dni] = (partes[1], partes[2], int(partes[3]))
    return padron


def busqueda_por_documento(padron, dni):
    if dni in padron:
        datos = padron[dni]
        return f"Nombre: {datos[0]} {datos[1]}, Edad: {datos[2]} años"
    else: 
        return None


def busqueda_por_apellido(padron, apellido):
    encontrados = []
    apellido_buscado = apellido.strip().lower()
    for dni, datos in padron.items():
        if datos[1].lower() == apellido_buscado:
            encontrados.append((dni, datos))
    return encontrados


def promedio_edad(padron):
    if not padron:
        return 0.0
    total = len(padron)
    suma = 0
    for dni, datos in padron.items():
        suma += datos[2]
    return suma / total


def mostrar_menu():
    print("\n" + "═" * 45)
    print("       SISTEMA DE GESTIÓN DE PADRÓN")
    print("═" * 45)
    print("  [1] Buscar por documento")
    print("  [2] Buscar por apellido")
    print("  [3] Calcular promedio de edades")
    print("  [0] Salir")
    print("─" * 45)


def main():
    padron = leer_padron("personas.csv")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n" + "·" * 45)
            entrada_dni = input("➤ Ingrese el número de documento: ").strip()
            if entrada_dni.isdigit():
                dni = int(entrada_dni)
                persona = busqueda_por_documento(padron, dni)

                if persona:
                    print("\n✔ Persona encontrada:")
                    print(f"  • {persona}")
                else:
                    print("\n✖ No existe ninguna persona registrada con ese documento.")
            else:
                print("\n⚠ Ingrese un valor numérico válido para el DNI.")

        elif opcion == "2":
            print("\n" + "·" * 45)
            apellido = input("➤ Ingrese el apellido a buscar: ").strip()
            coincidencias = busqueda_por_apellido(padron, apellido)

            if coincidencias:
                print(f"\n✔ Se encontraron {len(coincidencias)} resultado(s):")
                for dni, datos in coincidencias:
                    # datos[0] = nombre, datos[1] = apellido, datos[2] = edad
                    print(f"  • DNI: {dni} | {datos[0]} {datos[1]} ({datos[2]} años)")
            else:
                print("\n✖ No se registraron coincidencias para el apellido indicado.")

        elif opcion == "3":
            print("\n" + "·" * 45)
            promedio = promedio_edad(padron)
            print(f"✔ El promedio de edad general es: {promedio:.2f} años (total: {len(padron)} personas)")

        elif opcion == "0":
            print("\nSaliendo del sistema...")
            break

        else:
            print("\n⚠ Opción no válida. Por favor, ingrese un número del 0 al 3.")

        input("\nPresione [Enter] para continuar...")


main()