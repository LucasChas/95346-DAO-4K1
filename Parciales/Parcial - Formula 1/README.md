# Sistema de Gestión de Pilotos de Fórmula 1

La organización de un campeonato de Fórmula 1 necesita un sistema orientado a objetos para calcular cuánto cobra cada piloto al final de la temporada y obtener estadísticas del campeonato.

De **todos** los pilotos se conoce: el tipo, el número del auto (entero, identifica al piloto), el nombre, la escudería a la que pertenece, el sueldo base de la temporada y los puntos obtenidos en el campeonato. **Los puntos no pueden ser negativos**: si se intenta crear un piloto con puntos negativos se debe lanzar un `ValueError`.

Hay tres tipos de pilotos:

• **Titular**: se registra la cantidad de carreras ganadas. Cobra el sueldo base, más **$1000 por cada punto** obtenido, más **$50000 por cada victoria**. Si ganó **5 o más carreras** recibe un bonus del **10%** sobre el total anterior.

• **Suplente**: se registra la cantidad de carreras que disputó reemplazando a un titular. Cobra el sueldo base más **$20000 por cada carrera disputada**. Los puntos del suplente **no** suman dinero.

• **Novato**: se registra si ganó el premio a novato del año (`si` / `no`). Cobra el sueldo base más **$500 por cada punto** obtenido. Si ganó el premio a novato del año recibe un recargo del **25%** sobre el total anterior.

## Archivo pilotos.csv:

    • Tipo de piloto (1 = titular, 2 = suplente, 3 = novato)
    • Número del auto
    • Nombre
    • Escudería
    • Sueldo base
    • Puntos
    • Característica extra (victorias, carreras disputadas, premio novato si/no)

El archivo **no** tiene fila de encabezado.

Los pilotos, números de auto, escuderías, puntos, victorias y carreras disputadas corresponden a la temporada 2024 de F1 (simplificados: Bearman figura solo en Ferrari aunque también corrió para Haas). Los sueldos y el premio a novato del año son **ficticios**.

## Modelo de clases

Se deben respetar los siguientes nombres de módulos, clases, constructores y atributos (los tests dependen de ellos):

| Módulo | Clase | Constructor | Atributos |
|---|---|---|---|
| `piloto.py` | `Piloto` (abstracta) | `Piloto(tipo, numero, nombre, escuderia, sueldo_base, puntos)` | `tipo`, `numero`, `nombre`, `escuderia`, `sueldo_base`, `puntos` |
| `titular.py` | `Titular(Piloto)` | `Titular(numero, nombre, escuderia, sueldo_base, puntos, victorias)` | `tipo == 1`, `victorias` |
| `suplente.py` | `Suplente(Piloto)` | `Suplente(numero, nombre, escuderia, sueldo_base, puntos, carreras)` | `tipo == 2`, `carreras` |
| `novato.py` | `Novato(Piloto)` | `Novato(numero, nombre, escuderia, sueldo_base, puntos, premio)` | `tipo == 3`, `premio` (`"si"`/`"no"`) |
| `campeonato.py` | `Campeonato` | `Campeonato(nombre_archivo)` | `pilotos` (lista de `Piloto`) |

- `Piloto` debe ser una clase **abstracta** (no se puede instanciar) con el método abstracto `calcular_pago()`.
- Cada subclase implementa `calcular_pago()` según las reglas de arriba.
- Todos los pilotos implementan `__str__` mostrando, al menos, su nombre.
- `Campeonato` carga los pilotos desde el archivo en su constructor. Si el archivo no existe debe propagarse `FileNotFoundError`.

## Funcionalidades (métodos de `Campeonato`):

    1. Cargar los pilotos desde el archivo (en el constructor).
    2. calcular_promedio_puntos(): promedio ENTERO de los puntos de todos los pilotos.
    3. obtener_piloto_mejor_pago(): devolver el piloto que más cobra.
    4. calcular_total_pagos(): suma de lo que cobran todos los pilotos.
    5. contar_titulares_con_bonus(): cuántos titulares ganaron 5 o más carreras.
    6. contar_novatos_premiados(): cuántos novatos ganaron el premio a novato del año.
    7. cantidad_por_tipo(): diccionario con la cantidad de pilotos de cada tipo. Las claves deben ser "Titular", "Suplente" y "Novato".
    8. puntos_por_escuderia(): diccionario cuyas claves son los nombres de las escuderías y los valores la suma de puntos de sus pilotos (de todos los tipos).
    9. escuderia_campeona(): nombre de la escudería con más puntos en total.
    10. buscar_piloto(numero): devolver el piloto con ese número de auto, o None si no existe.
    11. ranking(n): lista con los NOMBRES de los n pilotos con más puntos, ordenada de mayor a menor. Si n es mayor que la cantidad de pilotos, se devuelven todos.

## Cómo probar

Implementar las clases en esta misma carpeta y ejecutar:

    pytest test_formula1.py -v
