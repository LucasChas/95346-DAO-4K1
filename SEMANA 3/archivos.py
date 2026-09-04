#Asi imprimo los datos de un archivo de una vez.
# archivo = open("./datos.txt")
# contenido = archivo.read()
# print(contenido)
# archivo.close()

#Asi leo linea a linea e imprimo
archivo = open("datos.txt")
linea = archivo.readline()
while linea:
    print(linea)
    linea = archivo.readline()
archivo.close()

### asi creo un archivo con esos datos:
nombres = ['Juan', 'María', 'Carlos', 'Laura']
archivo = open("nombres.txt", "w")
for nombre in nombres:
    archivo.write(nombre + '\n')
archivo.close()


