# Sistema de Gestión de Reservas de un Hotel

Un complejo hotelero de la ciudad necesita un sistema orientado a objetos para administrar las reservas de sus alojamientos y conocer cuánto se recauda por cada una.

De **todas** las reservas se conoce: el tipo, un código alfanumérico que la identifica, el nombre del huésped, el precio por noche y la cantidad de noches reservadas. El **costo base** de una reserva es `precio por noche * cantidad de noches`.

El hotel ofrece tres tipos de alojamiento:

• **Habitación estándar**: se registra si la reserva incluye desayuno (`si` / `no`). Si incluye desayuno se suman **$1500 por cada noche**. Si la estadía es de **más de 7 noches** se aplica un **descuento del 15%** sobre el total (costo base + desayunos).

• **Suite**: se registra la cantidad de servicios de spa contratados. A la suite se le suman **$4000 por cada servicio de spa**.

• **Cabaña**: se registra si el huésped viaja con mascota (`si` / `no`). Toda cabaña tiene un cargo fijo de limpieza de **$3000**. Si el huésped viaja con mascota se aplica un **recargo del 20%** sobre el total (costo base + limpieza).

## Archivo reservas.csv:

    • Tipo de reserva (1 = estándar, 2 = suite, 3 = cabaña)
    • Código
    • Huésped
    • Precio por noche
    • Cantidad de noches
    • Característica extra (desayuno si/no, cantidad de servicios de spa, mascota si/no)

El archivo **no** tiene fila de encabezado.

## Modelo de clases

Se deben respetar los siguientes nombres de módulos, clases, constructores y atributos (los tests dependen de ellos):

| Módulo | Clase | Constructor | Atributos |
|---|---|---|---|
| `reserva.py` | `Reserva` (abstracta) | `Reserva(tipo, codigo, huesped, precio_noche, noches)` | `tipo`, `codigo`, `huesped`, `precio_noche`, `noches` |
| `estandar.py` | `Estandar(Reserva)` | `Estandar(codigo, huesped, precio_noche, noches, desayuno)` | `tipo == 1`, `desayuno` (`"si"`/`"no"`) |
| `suite.py` | `Suite(Reserva)` | `Suite(codigo, huesped, precio_noche, noches, servicios_spa)` | `tipo == 2`, `servicios_spa` |
| `cabana.py` | `Cabana(Reserva)` | `Cabana(codigo, huesped, precio_noche, noches, mascota)` | `tipo == 3`, `mascota` (`"si"`/`"no"`) |
| `hotel.py` | `Hotel` | `Hotel(nombre_archivo)` | `reservas` (lista de `Reserva`) |

- `Reserva` debe ser una clase **abstracta** (no se puede instanciar) con el método abstracto `calcular_costo()`.
- Cada subclase implementa `calcular_costo()` según las reglas de arriba.
- Todas las reservas implementan `__str__` mostrando, al menos, su código.
- `Hotel` carga las reservas desde el archivo en su constructor. Si el archivo no existe debe propagarse `FileNotFoundError`.

## Funcionalidades (métodos de `Hotel`):

    1. Cargar las reservas desde el archivo (en el constructor).
    2. calcular_promedio_noches(): promedio ENTERO de la cantidad de noches de todas las reservas.
    3. obtener_reserva_mayor_costo(): devolver la reserva con mayor costo.
    4. calcular_recaudacion_total(): suma de los costos de todas las reservas.
    5. contar_estandar_con_descuento(): cuántas habitaciones estándar tienen más de 7 noches.
    6. contar_cabanas_con_mascota(): cuántas cabañas se reservaron con mascota.
    7. cantidad_por_tipo(): diccionario con la cantidad de reservas de cada tipo. Las claves deben ser "Estándar", "Suite" y "Cabaña".
    8. buscar_reserva(codigo): devolver la reserva con ese código, o None si no existe.
    9. codigos_por_rango_costo(minimo, maximo): lista con los códigos de las reservas cuyo costo esté entre minimo y maximo (ambos inclusive), en el mismo orden del archivo.

## Cómo probar

Implementar las clases en esta misma carpeta y ejecutar:

    pytest test_hotel.py -v
