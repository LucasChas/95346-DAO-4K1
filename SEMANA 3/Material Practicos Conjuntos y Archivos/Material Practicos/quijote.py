import string

def extraer_palabras_libro(nombre_archivo):
    palabras_unicas = set()
    # Signos comunes a limpiar de los bordes de cada palabra
    puntuacion = string.punctuation + "¿¡«»“”'’*—"

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            # .split() sin parámetros separa por cualquier espacio o salto de línea
            palabras = linea.split()
            for palabra in palabras:
                # Normalizamos a minúsculas y quitamos signos ortográficos en los extremos
                limpia = palabra.lower().strip(puntuacion)
                if limpia:
                    palabras_unicas.add(limpia)

    return palabras_unicas


palabras_libros = extraer_palabras_libro("quijote.txt")
#1) Cantidad de palabras únicas (sin repetición) del libro.
print(f"Cantidad de palabras no repetidas (libro): {len(palabras_libros)}")

#2) Cantidad de palabras del diccionario.
palabras_diccionario = extraer_palabras_libro("words_alpha.txt")
print(f"Cantidad de palabras no repetidas (diccionario): {len(palabras_diccionario)}")

#3) Cantidad de palabras del libro que no existen en el diccionario. 
palabras_no_encontradas = palabras_libros - palabras_diccionario
cantidad = len(palabras_no_encontradas)
print(f"Cantidad de palabras del libro que no existen en el diccionario: {cantidad}")

#4) Listado ordenados de todas las palabras que no existen.
lista_ordenada = sorted(palabras_no_encontradas)
for palabra in lista_ordenada:
    print(palabra)