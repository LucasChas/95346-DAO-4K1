"""Tests del parcial Formula 1.
Uso:
    pytest test_formula1.py -v
"""

import sys
from pathlib import Path

import pytest

CARPETA = Path(__file__).resolve().parent
if str(CARPETA) not in sys.path:
    sys.path.insert(0, str(CARPETA))

ARCHIVO = str(CARPETA / "pilotos.csv")

from piloto import Piloto  # noqa: E402
from titular import Titular  # noqa: E402
from suplente import Suplente  # noqa: E402
from novato import Novato  # noqa: E402
from campeonato import Campeonato  # noqa: E402


@pytest.fixture
def campeonato():
    return Campeonato(ARCHIVO)


# ---------------------------------------------------------------------------
# Constructor / carga del archivo
# ---------------------------------------------------------------------------

def test_constructor_campeonato(campeonato):
    assert campeonato is not None
    assert len(campeonato.pilotos) == 9

def test_constructor_archivo_inexistente():
    with pytest.raises(FileNotFoundError):
        Campeonato("archivo_inexistente.csv")

def test_orden_de_carga(campeonato):
    numeros = [piloto.numero for piloto in campeonato.pilotos]
    assert numeros == [7, 12, 23, 31, 40, 45, 50, 55, 62]

def test_tipos_numericos_cargados(campeonato):
    primero = campeonato.pilotos[0]
    assert primero.numero == 7
    assert isinstance(primero.numero, int)
    assert primero.sueldo_base == 300000
    assert primero.puntos == 410
    assert primero.victorias == 8
    assert isinstance(primero.victorias, int)
    suplente = campeonato.pilotos[4]
    assert suplente.carreras == 4
    assert isinstance(suplente.carreras, int)


# ---------------------------------------------------------------------------
# Herencia, abstraccion y validaciones
# ---------------------------------------------------------------------------

def test_herencia_pilotos():
    assert issubclass(Titular, Piloto)
    assert issubclass(Suplente, Piloto)
    assert issubclass(Novato, Piloto)

def test_piloto_es_abstracto():
    with pytest.raises(TypeError):
        Piloto(1, 99, "Nadie", "Ninguna", 1000, 0)

def test_composicion_campeonato_pilotos(campeonato):
    assert hasattr(campeonato, "pilotos")
    for piloto in campeonato.pilotos:
        assert isinstance(piloto, Piloto)

def test_clases_segun_tipo(campeonato):
    for piloto in campeonato.pilotos:
        if piloto.tipo == 1:
            assert isinstance(piloto, Titular)
        elif piloto.tipo == 2:
            assert isinstance(piloto, Suplente)
        else:
            assert isinstance(piloto, Novato)

def test_puntos_negativos_titular():
    with pytest.raises(ValueError):
        Titular(1, "Error", "Ferrari", 100000, -1, 0)

def test_puntos_negativos_suplente():
    with pytest.raises(ValueError):
        Suplente(2, "Error", "Ferrari", 100000, -5, 1)

def test_puntos_negativos_novato():
    with pytest.raises(ValueError):
        Novato(3, "Error", "Ferrari", 100000, -10, "no")

def test_cero_puntos_es_valido():
    assert Suplente(45, "Franco Benitez", "Red Bull", 80000, 0, 0).puntos == 0


# ---------------------------------------------------------------------------
# Atributos
# ---------------------------------------------------------------------------

def test_atributos_titular():
    titular = Titular(7, "Tomas Almada", "Red Bull", 300000, 410, 8)
    assert titular.tipo == 1
    assert titular.numero == 7
    assert titular.nombre == "Tomas Almada"
    assert titular.escuderia == "Red Bull"
    assert titular.sueldo_base == 300000
    assert titular.puntos == 410
    assert titular.victorias == 8

def test_atributos_suplente():
    suplente = Suplente(40, "Santiago Lucero", "Ferrari", 90000, 6, 4)
    assert suplente.tipo == 2
    assert suplente.carreras == 4

def test_atributos_novato():
    novato = Novato(50, "Lucia Ferreyra", "Williams", 120000, 48, "si")
    assert novato.tipo == 3
    assert novato.premio == "si"

def test_str_incluye_nombre():
    assert "Tomas Almada" in str(Titular(7, "Tomas Almada", "Red Bull", 300000, 410, 8))
    assert "Santiago Lucero" in str(Suplente(40, "Santiago Lucero", "Ferrari", 90000, 6, 4))
    assert "Lucia Ferreyra" in str(Novato(50, "Lucia Ferreyra", "Williams", 120000, 48, "si"))


# ---------------------------------------------------------------------------
# calcular_pago de cada tipo
# ---------------------------------------------------------------------------

def test_titular_con_bonus():
    # (300000 + 1000 * 410 + 50000 * 8) = 1110000 -> +10%
    assert Titular(7, "Tomas Almada", "Red Bull", 300000, 410, 8).calcular_pago() == pytest.approx(1221000)

def test_titular_sin_bonus():
    # 250000 + 1000 * 320 + 50000 * 3
    assert Titular(12, "Bruno Salvatierra", "Ferrari", 250000, 320, 3).calcular_pago() == pytest.approx(720000)

def test_titular_5_victorias_tiene_bonus():
    # (200000 + 350000 + 250000) = 800000 -> +10%
    assert Titular(23, "Ignacio Paredes", "McLaren", 200000, 350, 5).calcular_pago() == pytest.approx(880000)

def test_titular_4_victorias_no_tiene_bonus():
    assert Titular(99, "Borde", "Alpine", 100000, 0, 4).calcular_pago() == pytest.approx(300000)

def test_suplente_con_carreras():
    # 90000 + 20000 * 4 (los puntos no suman)
    assert Suplente(40, "Santiago Lucero", "Ferrari", 90000, 6, 4).calcular_pago() == pytest.approx(170000)

def test_suplente_sin_carreras():
    assert Suplente(45, "Franco Benitez", "Red Bull", 80000, 0, 0).calcular_pago() == pytest.approx(80000)

def test_novato_premiado():
    # (120000 + 500 * 48) = 144000 -> +25%
    assert Novato(50, "Lucia Ferreyra", "Williams", 120000, 48, "si").calcular_pago() == pytest.approx(180000)

def test_novato_no_premiado():
    # 110000 + 500 * 12
    assert Novato(55, "Emiliano Rojas", "Williams", 110000, 12, "no").calcular_pago() == pytest.approx(116000)


# ---------------------------------------------------------------------------
# Funcionalidades de Campeonato
# ---------------------------------------------------------------------------

def test_calcular_promedio_puntos(campeonato):
    # 1366 puntos / 9 pilotos = 151.77 -> 151
    promedio = campeonato.calcular_promedio_puntos()
    assert promedio == 151
    assert isinstance(promedio, int)

def test_obtener_piloto_mejor_pago(campeonato):
    piloto = campeonato.obtener_piloto_mejor_pago()
    assert piloto.numero == 7
    assert piloto.nombre == "Tomas Almada"
    assert piloto.calcular_pago() == pytest.approx(1221000)

def test_calcular_total_pagos(campeonato):
    assert campeonato.calcular_total_pagos() == pytest.approx(3880750)

def test_contar_titulares_con_bonus(campeonato):
    assert campeonato.contar_titulares_con_bonus() == 2

def test_contar_novatos_premiados(campeonato):
    assert campeonato.contar_novatos_premiados() == 2

def test_cantidad_por_tipo(campeonato):
    assert campeonato.cantidad_por_tipo() == {"Titular": 4, "Suplente": 2, "Novato": 3}

def test_puntos_por_escuderia(campeonato):
    assert campeonato.puntos_por_escuderia() == {
        "Red Bull": 410,
        "Ferrari": 326,
        "McLaren": 540,
        "Williams": 60,
        "Alpine": 30,
    }

def test_escuderia_campeona(campeonato):
    assert campeonato.escuderia_campeona() == "McLaren"

def test_buscar_piloto_existente(campeonato):
    piloto = campeonato.buscar_piloto(62)
    assert piloto is not None
    assert piloto.nombre == "Joaquin Vera"
    assert isinstance(piloto, Novato)

def test_buscar_piloto_inexistente(campeonato):
    assert campeonato.buscar_piloto(99) is None

def test_ranking_top_3(campeonato):
    assert campeonato.ranking(3) == ["Tomas Almada", "Ignacio Paredes", "Bruno Salvatierra"]

def test_ranking_todos(campeonato):
    assert campeonato.ranking(20) == [
        "Tomas Almada",
        "Ignacio Paredes",
        "Bruno Salvatierra",
        "Mateo Quiroga",
        "Lucia Ferreyra",
        "Joaquin Vera",
        "Emiliano Rojas",
        "Santiago Lucero",
        "Franco Benitez",
    ]

def test_ranking_no_modifica_orden_original(campeonato):
    campeonato.ranking(3)
    assert [piloto.numero for piloto in campeonato.pilotos] == [7, 12, 23, 31, 40, 45, 50, 55, 62]
