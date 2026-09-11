# 1.6.2 Procesamiento de temperaturas en una lista
# Ingresar un conjunto de temperaturas en una lista, finalizar la carga cuando
# se reciba un 50. Sólo aceptar temperaturas entre -20 y 49 grados.
# Calcular y mostrar:
# • Cantidad de días con temperatura bajo cero
# • Promedio de temperaturas
# • Promedio de temperaturas de los días cálidos, es decir con temp. mayor
# a 20
# • Mostrar “Si” o “No” para indicar si hubo algún día con más de 40 grados.
# • La mayor temperatura de los días que no fueron cálidos
# • Cantidad de días con temperatura menor al promedio


def ingresar_numero(mensaje,minimo,maximo):
    temperatura = float(input(mensaje))
    while not minimo <= temperatura <= maximo:
        print(f"Debe ingresar un valor entre {minimo} y {maximo}")
        temperatura = float(input(mensaje))
    return temperatura

def cargar_temperaturas():
    temperaturas = []
    temperatura = ingresar_numero("Ingresa una temperatura entre -20°C y 49°C: Finaliza con 50: ", -20,50)
    while temperatura != 50:
        temperaturas.append(temperatura)
        temperatura = ingresar_numero("Ingresa una temperatura entre -20°C y 49°C: Finaliza con 50: ", -20,50)
    return temperaturas

# • Cantidad de días con temperatura bajo cero
def cantidad_dias_bajo_cero(lista):
    cantidad = 0
    for i in lista:
        if i < 0:
            cantidad+= 1
    return cantidad

# • Promedio de temperaturas
def promedio(lista):
    total = len(lista)
    if total == 0:
        return 0
    suma = 0
    for i in lista:
       suma += i
    return suma / total

# • Promedio de temperaturas de los días cálidos, es decir con temp. mayor
# a 20

def promedio_mayor_20(lista):
    total = 0
    suma = 0
    for i in lista:
       if i > 20:
        suma += i
        total += 1
    if total == 0:
        return 0
    return suma / total

#• Mostrar “Si” o “No” para indicar si hubo algún día con más de 40 grados.
def existe_40_grados(lista):
    for i in lista:
        if i > 40:
            return True
    return False

# • La mayor temperatura de los días que no fueron cálidos
def mayor_temperatura(lista):
    mayor = None
    for i in lista:
        if i <= 20:
            if mayor is None or i > mayor:
                mayor = i
    return mayor

# • Cantidad de días con temperatura menor al promedio
def dias_temperatura_menor_promedio(lista, promedio):
    cantidad = 0
    for i in lista:
        if i < promedio:
            cantidad += 1
    return cantidad

def calcular(lista):
    dias_bajo_cero = cantidad_dias_bajo_cero(lista)
    promedio_todos = promedio(lista)
    promedio_20 = promedio_mayor_20(lista)
    dias_menor_promedio = dias_temperatura_menor_promedio(lista,promedio_todos)
    hubo_40_grados = existe_40_grados(lista)
    mayor_calido = mayor_temperatura(lista)


    print(f"Hubo {dias_bajo_cero} dias con temperatura bajo cero")
    print(f"El promedio de temperaturas fue de: {promedio_todos}")
    if (promedio_20 != 0):
        print(f"y de los dias calidos fue de: {promedio_20}")  
    print("¿Hubo dias con mas de 40 grados?: ", "Si" if hubo_40_grados else "No")
    if mayor_calido: 
        print(f"La mayor temperatura de los dias calidaos fue de: {mayor_calido}")
    else:
        print("Todos los dias fueron calidos")
    print(f"La cantidad de dias por debajo del promedio fue de: {dias_menor_promedio}")

def main():
    lista_temperaturas = cargar_temperaturas()
    calcular(lista_temperaturas)

main()