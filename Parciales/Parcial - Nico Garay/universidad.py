import csv
from teorico import Teorico
from practico import Practico
from online import Online
#1)
def leer_csv(nombre):
    
    cursos = []
    archivo = open(nombre, "r", encoding="utf8")
    lector = csv.reader(archivo)
    for fila in lector:
        if not fila:
            continue
        tipo = int(fila[0])
        codigo = fila[1]
        materia = fila[2]
        precio = float(fila[3])
        cant_a = int(fila[4])
        if tipo == 1:
            curso = Teorico(tipo,codigo,materia,precio, cant_a)
        elif tipo == 2:
            extra = fila[5]
            curso = Practico(tipo,codigo, materia, precio, cant_a, extra)
        elif tipo == 3:
            extra = fila[5].strip().lower() in ("true", "1")
            curso = Online(tipo,codigo, materia, precio, cant_a, extra)
        else:
            continue
        cursos.append(curso)

    return cursos

#2)
def calcular_promedio(cursos): 
    if len(cursos) == 0:
        return 0
    suma_precios = 0.0
    cantidad_cursos = len(cursos)
    for curso in cursos:
        suma_precios += curso.calcular_precio()

    return round(suma_precios//cantidad_cursos)


#3)
def obtener_curso_mas_caro(cursos):
    if len(cursos) == 0:
        return None

    curso_mas_caro = cursos[0]
    precio_mas_alto = cursos[0].calcular_precio()

    for curso in cursos[1:]:
        precio_actual = curso.calcular_precio()
        if precio_actual > precio_mas_alto:
            precio_mas_alto = precio_actual
            curso_mas_caro = curso

    return curso_mas_caro

#4)
def calcular_ingreso_total(cursos):
    total = 0.0

    for curso in cursos:
        total = total + curso.calcular_precio_total()

    return total

#5)
def contar_teoricos_mas_50_alumnos(cursos):
    contador = 0
    for curso in cursos:
        if curso.tipo_curso == 1 and curso.cant_alumnos > 50:
            contador += 1
    return contador

#6)
def contar_online_con_tutorias(cursos):
    contador = 0
    for curso in cursos:
        if curso.tipo_curso == 3 and curso.tutorias_personalizadas is True:
            contador += 1
    return contador

#7)
def contar_cursos_por_tipo(cursos):
    diccionario_conteos = {
        "Teórico": 0,
        "Práctico": 0,
        "Online": 0
    }

    for curso in cursos:
        if curso.tipo_curso == 1:
            diccionario_conteos["Teórico"] = diccionario_conteos["Teórico"] + 1
        elif curso.tipo_curso == 2:
            diccionario_conteos["Práctico"] = diccionario_conteos["Práctico"] + 1
        elif curso.tipo_curso == 3:
            diccionario_conteos["Online"] = diccionario_conteos["Online"] + 1

    return diccionario_conteos


def main():
    # 1. Cargar cursos
    lista_cursos = leer_csv("cursos.csv")
    print(f"Total de cursos cargados: {len(lista_cursos)}\n")
    print(f"cursos cargados:")
    for curso in lista_cursos:
        print(curso)
    print("-"*100)
    # 2. Promedio entero
    promedio = calcular_promedio(lista_cursos)
    print(f"2. Promedio entero de precio por estudiante: ${promedio}")
    print("-"*100)
    # 3. Curso más caro
    mas_caro = obtener_curso_mas_caro(lista_cursos)
    if mas_caro is not None:
        print(f"3. Curso más caro: {mas_caro.nombre_curso} (${mas_caro.calcular_precio():.2f})")
    print("-"*100)
    # 4. Ingreso total
    ingreso_total = calcular_ingreso_total(lista_cursos)
    print(f"4. Ingreso total de la universidad: ${ingreso_total:.2f}")
    print("-"*100)
    # 5. Teóricos > 50 alumnos
    cant_teoricos = contar_teoricos_mas_50_alumnos(lista_cursos)
    print(f"5. Cursos teóricos con más de 50 alumnos: {cant_teoricos}")
    print("-"*100)
    # 6. Online con tutorías
    cant_online = contar_online_con_tutorias(lista_cursos)
    print(f"6. Cursos online con tutorías: {cant_online}")
    print("-"*100)
    # 7. Conteo por tipo
    conteo_tipos = contar_cursos_por_tipo(lista_cursos)
    print(f"7. Cantidad de cursos por tipo: {conteo_tipos}")

if __name__ == "__main__":
    main()
