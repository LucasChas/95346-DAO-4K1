#Desarrollar un programa que lea todo el contenido del archivo numeros.txt
# que contiene múltiples líneas de texto, cada una de ellas con un número
# entero. Al leer el archivo se debe almacenar todos los números en una lista. A
# continuación el programa debe manipular los números cargados en la lista
# para:
# • Calcular e imprimir el promedio de todos los números
# • Calcular e imprimir la cantidad de números mayores al promedio
# • Generar y mostrar una nueva lista que contenga todos los números pares


#meto los numeros en la lista
archivo = open("numeros.txt")

def extraer_numeros(archivo):
    lista_numeros = []
    
    while True:
        numero = archivo.readline() 
        if not numero: 
            break
        n = int(numero[:-1])
        lista_numeros.append(n)
    archivo.close()
    return lista_numeros

    
def promedio (lista_numeros):
    suma = 0
    promedio = 0
    for i in lista_numeros:
        suma += 1
        promedio += i
    return promedio/suma 

def mayor_promedio (lista_numeros, promedio):
    contador = 0
    for i in lista_numeros: 
        if i > promedio:
            contador+=1
    return contador

def pares(lista_numeros):
    lista = []
    for i in lista_numeros:
        if i%2 == 0:
            lista.append(i)
    return lista

if __name__ == "__main__":
    lista = extraer_numeros(archivo)
    print("La lista de numeros es: ", lista)
    p = promedio(lista)
    print("El promedio es:", promedio(lista))
    cantidad_mayor = print("la cantidad de numeros mayores al promedio es de:",mayor_promedio(lista,p))
    lista_pares = print("La lista de numeros pares es:", pares(lista))
