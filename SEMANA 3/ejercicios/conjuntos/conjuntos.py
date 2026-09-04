# Lista con elementos duplicados
lista = [1, 2, 3, 4, 2, 3, 5, 6, 1, 7, 8, 5, 9]
# Convertir la lista en un conjunto
# para eliminar duplicados
conjunto = set(lista)
# Convertir el conjunto nuevamente a una lista
lista_sin_duplicados = list(conjunto)
# Imprimir la lista sin duplicados
print(lista_sin_duplicados)
#-------------------------------------------------

# Conjunto de nombres de personas del curso A
curso_a = {"Juan", "María", "Pedro", "Luisa", "Ana"}
# Conjunto de nombres de personas del curso B
curso_b = {"Pedro", "Ana", "Sofía", "Carlos"}
# Unión: personas inscriptas en al menos uno de los cursos
union = curso_a.union(curso_b)
print(union)
# {'Juan', 'Carlos', 'María', 'Pedro', 'Luisa', 'Ana', 'Sofía'}
# Intersección: personas inscriptas en ambos cursos
interseccion = curso_a.intersection(curso_b)
print(interseccion)
# {'Ana', 'Pedro'}
# Diferencia: inscriptos sólo en el curso A
diferencia = curso_a.difference(curso_b)
print(diferencia)
# {'María', 'Luisa', 'Juan'}
# Diferencia simétrica: inscriptos en
# uno de los cursos, pero no en ambos
diferencia_simetrica = curso_a


#------------------------------------
diccionario = {1: "Lunes", 2: "Martes", 3: "Miércoles"}
for numero, nombre in diccionario.items():
    print(f"El día {numero} se llama {nombre}")