#Desarrollar un programa que lea todo el contenido del archivo numeros.txt
# que contiene múltiples líneas de texto, cada una de ellas con un número
# entero. Al leer el archivo se debe almacenar todos los números en una lista. A
# continuación el programa debe manipular los números cargados en la lista
# para:
# • Calcular e imprimir el promedio de todos los números
# • Calcular e imprimir la cantidad de números mayores al promedio
# • Generar y mostrar una nueva lista que contenga todos los números pares

archivo = open("numeros.txt")
lista_numeros = []
numero = archivo.readline()
#meto los numeros en la lista
while numero:
    lista_numeros.append(numero)
    numero = archivo.readline()

print(lista_numeros)
    
    