from campeonato import Campeonato

def main():
    nombre_archivo = "pilotos.csv"
    campeonato = Campeonato(nombre_archivo)

    print("=" * 60)
    print("       SISTEMA DE GESTIÓN DE PILOTOS - FÓRMULA 1")
    print("=" * 60)

    # 1. Total de pilotos cargados
    print(f"\n1. Pilotos cargados: {len(campeonato.pilotos)}")

    # 2. Promedio entero de puntos
    promedio = campeonato.calcular_promedio_puntos()
    print(f"2. Promedio de puntos por piloto: {promedio}")

    # 3. Piloto mejor pago
    mejor_pago = campeonato.obtener_piloto_mejor_pago()
    if mejor_pago:
        print(f"3. Piloto mejor pago: {mejor_pago.nombre} (${mejor_pago.calcular_pago():,.2f})")

    # 4. Total de pagos a todos los pilotos
    total_pagos = campeonato.calcular_total_pagos()
    print(f"4. Total a pagar a todos los pilotos: ${total_pagos:,.2f}")

    # 5. Titulares con bonus (5 o más victorias)
    titulares_bonus = campeonato.contar_titulares_con_bonus()
    print(f"5. Titulares con bonus por 5+ victorias: {titulares_bonus}")

    # 6. Novatos premiados (premio al novato del año)
    novatos_premio = campeonato.contar_novatos_premiados()
    print(f"6. Novatos premiados como novato del año: {novatos_premio}")

    # 7. Cantidad de pilotos por tipo
    conteo_tipos = campeonato.cantidad_por_tipo()
    print("\n7. Cantidad de pilotos por categoría:")
    for tipo, cantidad in conteo_tipos.items():
        print(f"   - {tipo}: {cantidad}")

    # 8. Puntos por escudería
    puntos_escuderia = campeonato.puntos_por_escuderia()
    print("\n8. Puntos totales por escudería:")
    for escuderia, puntos in puntos_escuderia.items():
        print(f"   - {escuderia}: {puntos} pts")

    # 9. Escudería campeona
    campeona = campeonato.escuderia_campeona()
    print(f"\n9. Escudería campeona: {campeona} ({puntos_escuderia.get(campeona, 0)} pts)")

    # 10. Búsqueda de piloto por número (ejemplos: existente y no existente)
    print("\n10. Búsqueda de piloto por número:")
    for num in [43, 99]:
        piloto = campeonato.buscar_piloto(num)
        if piloto:
            print(f"   - Auto #{num}: Encontrado -> {piloto.nombre} ({piloto.escuderia})")
        else:
            print(f"   - Auto #{num}: No encontrado (None)")

    # 11. Ranking de pilotos (Top 3 y Top 5)
    print("\n11. Ranking:")
    print("   - Top 3 pilotos con más puntos:", campeonato.ranking(3))
    print("   - Top 5 pilotos con más puntos:", campeonato.ranking(5))
    print("=" * 60)

if __name__ == "__main__":
    main()