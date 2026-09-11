# Practico con Números en archivo 
# Del archivo numeros.txt que contiene un número entero por cada línea, generar un conjunto que 
# contenga todos los números del archivo y desde el conjunto calcular e informar: 
# • Cantidad de números no repetidos 
# • Suma de todos los números 
# • Cantidad de impares 
# • Promedio de pares 

def extraer_datos(nombre):
    numeros = set()
    archivo = open(nombre)
    for linea in archivo:
        linea = linea.strip()
        if linea:
            numeros.add(int(linea))
    return numeros


def suma_numeros(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma

def impares(lista):
    suma = 0
    for i in lista:
        if i %2 != 0:
            suma += 1
    return suma

def promedio_pares(lista):
    suma_pares = 0
    suma = 0
    for i in lista:
        if i %2 == 0:
            suma_pares += i
            suma += 1
    return suma_pares/suma
conjunto = extraer_datos("./numeros.txt")

cantidad_no_repetidos = len(conjunto)
print(f"Cantidad de números no repetidos: {cantidad_no_repetidos}")
print(f"la suma de todos los numeros es de: ", suma_numeros(conjunto))
print(f"La cantidad de impares es de: {impares(conjunto)}")
print(f"Promedio de los pares es de: {promedio_pares(conjunto)}")




