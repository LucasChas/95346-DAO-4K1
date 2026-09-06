# El archivo tips.csv contiene los datos de las propinas recibidas por los emplea-
# dos de una pizzería en New York.

# El archivo contiene los siguientes campos separados por comas
# • total_bill: Importe total del servicio
# • tip: Importe de la propina
# • sex: Sexo del cliente
# • smoker: El cliente es fumador (Yes, No)
# • day: Día (Juev, Vie, Sab, Dom)
# • time: Horario (Almuerzo, Cena)
# • size: Tamaño de la mesa (comensales)
# Se requiere desarrollar un programa que desde los datos del archivo
# informe:
# • ¿Quién paga más propinas?¿Hombres o mujeres?
# • ¿Cuáles son los días más ‘lentos’, con menos propinas?
# • ¿Cuál es el promedio de las propinas?
# • ¿Cuándo se vendió la orden más grande (qué día y en qué turno)?

def extraer_datos(nombre):
    archivo = open(nombre)
    lista = []
    archivo.readline() #descarta la columna
    for i in archivo.readlines():
        n = i[:-1].split(",")
        lista.append(n)
    return lista

#¿Quién paga más propinas?¿Hombres o mujeres?
def quien_paga_mas(lista):
    lista_acum = [0]*2
    
    for i in lista:
        if i[2] == "Hombre":
            lista_acum[0] += float(i[1])
        else:
            lista_acum[1]+= float(i[1])
    return lista_acum

#¿Cuáles son los días más ‘lentos’, con menos propinas?
def dias_mas_lentos(lista):
    lista_contadores = [0]*4
    for i in lista:
        if i[4] == "Juev":
            lista_contadores[0] += float(i[1])
        elif i[4] == "Vie":
            lista_contadores[1] += float(i[1])
        elif i[4] == "Sab":
            lista_contadores[2] += float(i[1])
        else: 
            lista_contadores[3] += float(i[1])
    return lista_contadores


#¿Cuál es el promedio de las propinas?
def promedio_propinas(lista):
    acum_propina = 0
    total = len(lista)
    for i in lista:
        acum_propina += float(i[1])
    return acum_propina/total

#¿Cuándo se vendió la orden más grande (qué día y en qué turno)?
def orden_mas_grande(lista):
    mayor_monto = None
    dia_mayor = ""
    turno_mayor = ""
    for i in lista:
        monto_actual = float(i[0])
        if mayor_monto is None or monto_actual > mayor_monto:
            mayor_monto = monto_actual
            dia_mayor = i[4]
            turno_mayor = i[5]
    return dia_mayor, turno_mayor, mayor_monto




def main ():
    lista = extraer_datos('./tips.csv')
    paga_mas = quien_paga_mas(lista)
    promedio = promedio_propinas(lista)
    dias_lentos = dias_mas_lentos(lista)
    orden_grande = orden_mas_grande(lista)

    print(f"Analisis del dataset - Propinas...")
    print("-"*70)
    if paga_mas[0] > paga_mas[1]:
        print(f"Los Hombres pagan mejor propina, siendo el total de : ${paga_mas[0]:3f}")
    else:
        print(f"Las Mujeres pagan mejor propina, siendo el total de : ${paga_mas[1]:3f}")
    print("-"*70)
    print(f"El promedio de propinas es de: ${promedio:3f}")
    print("-"*70)


    dias = ["Jueves", "Viernes", "Sabado", "Domingo"]

    menor_monto = min(dias_lentos)
    indice_menor = dias_lentos.index(menor_monto)
    dia_menor = dias[indice_menor]

    print(f"El día más lento fue {dia_menor} con un total de propinas de ${menor_monto:.3f}")
    print("-"*70)
    print(f"La orden con mayor venta fue de: ${orden_grande[2]}, del dia: {orden_grande[0]} y en el turno {orden_grande[1]}" )
main()