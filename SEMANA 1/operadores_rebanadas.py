titulo = "Lucas"
print(titulo[0])
print(titulo[1])
print(titulo[2])
print(titulo[3])
print(titulo[4])
print("-"*50)
print(titulo[-1])
print(titulo[-2])
print(titulo[-3])
print(titulo[-4])
print(titulo[-5])

#Operadores de rebanadas
print("-"*50)
titulo = "Paisaje"
print(titulo[1:3]) # imprime "ai"
print(titulo[:3]) # imprime "Pai"
print(titulo[3:]) # imprime "saje"
print("-"*50)

#Para ello se puede incluir un segundo símbolo
# de dos puntos y a continuación un número entero estableciendo que se corten
# los elementos desde el índice inicial y se salteen los siguientes. Así, con un
# salto de 2, se extraen las posiciones alternadas, mientras que con un salto de
# -1 se recorre la secuencia hacia atrás. De esta manera, utilizando una rebana-
# da sin indicar inicio ni final y con salto -1, se obtiene una nueva secuencia
# inviertiendo la primera.
titulo = "Paisaje"
print(titulo[::2]) # imprime "Piae" -alterna desde el inicio de a 2.
print(titulo[5:0:-1]) # imprime "jasia"
print(titulo[:-1])

#el motivo en los archivos:
numero='40\n'
print(int(numero[:-1])) # - Corto el \n de una con esto.

