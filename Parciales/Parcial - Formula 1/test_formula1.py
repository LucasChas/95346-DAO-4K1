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
    assert len(campeonato.pilotos) == 11

def test_constructor_archivo_inexistente():
    with pytest.raises(FileNotFoundError):
        Campeonato("archivo_inexistente.csv")

def test_orden_de_carga(campeonato):
    numeros = [piloto.numero for piloto in campeonato.pilotos]
    assert numeros == [1, 4, 16, 81, 55, 63, 44, 38, 30, 43, 7]

def test_tipos_numericos_cargados(campeonato):
    primero = campeonato.pilotos[0]
    assert primero.numero == 1
    assert isinstance(primero.numero, int)
    assert primero.sueldo_base == 550000
    assert primero.puntos == 437
    assert primero.victorias == 9
    assert isinstance(primero.victorias, int)
    suplente = campeonato.pilotos[7]
    assert suplente.carreras == 3
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
    assert Novato(7, "Jack Doohan", "Alpine", 40000, 0, "no").puntos == 0


# ---------------------------------------------------------------------------
# Atributos
# ---------------------------------------------------------------------------

def test_atributos_titular():
    titular = Titular(1, "Max Verstappen", "Red Bull", 550000, 437, 9)
    assert titular.tipo == 1
    assert titular.numero == 1
    assert titular.nombre == "Max Verstappen"
    assert titular.escuderia == "Red Bull"
    assert titular.sueldo_base == 550000
    assert titular.puntos == 437
    assert titular.victorias == 9

def test_atributos_suplente():
    suplente = Suplente(38, "Oliver Bearman", "Ferrari", 50000, 7, 3)
    assert suplente.tipo == 2
    assert suplente.carreras == 3

def test_atributos_novato():
    novato = Novato(43, "Franco Colapinto", "Williams", 70000, 5, "si")
    assert novato.tipo == 3
    assert novato.premio == "si"

def test_str_incluye_nombre():
    assert "Max Verstappen" in str(Titular(1, "Max Verstappen", "Red Bull", 550000, 437, 9))
    assert "Oliver Bearman" in str(Suplente(38, "Oliver Bearman", "Ferrari", 50000, 7, 3))
    assert "Franco Colapinto" in str(Novato(43, "Franco Colapinto", "Williams", 70000, 5, "si"))


# ---------------------------------------------------------------------------
# calcular_pago de cada tipo
# ---------------------------------------------------------------------------

def test_titular_con_bonus():
    # (550000 + 1000 * 437 + 50000 * 9) = 1437000 -> +10%
    assert Titular(1, "Max Verstappen", "Red Bull", 550000, 437, 9).calcular_pago() == pytest.approx(1580700)

def test_titular_sin_bonus():
    # 300000 + 1000 * 374 + 50000 * 4
    assert Titular(4, "Lando Norris", "McLaren", 300000, 374, 4).calcular_pago() == pytest.approx(874000)

def test_titular_5_victorias_tiene_bonus():
    # (100000 + 0 + 250000) = 350000 -> +10%
    assert Titular(99, "Borde", "Alpine", 100000, 0, 5).calcular_pago() == pytest.approx(385000)

def test_titular_4_victorias_no_tiene_bonus():
    assert Titular(99, "Borde", "Alpine", 100000, 0, 4).calcular_pago() == pytest.approx(300000)

def test_suplente_con_carreras():
    # 60000 + 20000 * 6 (los puntos no suman)
    assert Suplente(30, "Liam Lawson", "RB", 60000, 4, 6).calcular_pago() == pytest.approx(180000)

def test_suplente_sin_carreras():
    assert Suplente(99, "Sin carreras", "Haas", 50000, 0, 0).calcular_pago() == pytest.approx(50000)

def test_novato_premiado():
    # (70000 + 500 * 5) = 72500 -> +25%
    assert Novato(43, "Franco Colapinto", "Williams", 70000, 5, "si").calcular_pago() == pytest.approx(90625)

def test_novato_no_premiado():
    # 40000 + 500 * 0
    assert Novato(7, "Jack Doohan", "Alpine", 40000, 0, "no").calcular_pago() == pytest.approx(40000)


# ---------------------------------------------------------------------------
# Funcionalidades de Campeonato
# ---------------------------------------------------------------------------

def test_calcular_promedio_puntos(campeonato):
    # 2233 puntos / 11 pilotos = 203
    promedio = campeonato.calcular_promedio_puntos()
    assert promedio == 203
    assert isinstance(promedio, int)

def test_obtener_piloto_mejor_pago(campeonato):
    piloto = campeonato.obtener_piloto_mejor_pago()
    assert piloto.numero == 1
    assert piloto.nombre == "Max Verstappen"
    assert piloto.calcular_pago() == pytest.approx(1580700)

def test_calcular_total_pagos(campeonato):
    assert campeonato.calcular_total_pagos() == pytest.approx(6411325)

def test_contar_titulares_con_bonus(campeonato):
    assert campeonato.contar_titulares_con_bonus() == 1

def test_contar_novatos_premiados(campeonato):
    assert campeonato.contar_novatos_premiados() == 1

def test_cantidad_por_tipo(campeonato):
    assert campeonato.cantidad_por_tipo() == {"Titular": 7, "Suplente": 2, "Novato": 2}

def test_puntos_por_escuderia(campeonato):
    assert campeonato.puntos_por_escuderia() == {
        "Red Bull": 437,
        "McLaren": 666,
        "Ferrari": 653,
        "Mercedes": 468,
        "RB": 4,
        "Williams": 5,
        "Alpine": 0,
    }

def test_escuderia_campeona(campeonato):
    assert campeonato.escuderia_campeona() == "McLaren"

def test_buscar_piloto_existente(campeonato):
    piloto = campeonato.buscar_piloto(43)
    assert piloto is not None
    assert piloto.nombre == "Franco Colapinto"
    assert isinstance(piloto, Novato)

def test_buscar_piloto_inexistente(campeonato):
    assert campeonato.buscar_piloto(99) is None

def test_ranking_top_3(campeonato):
    assert campeonato.ranking(3) == ["Max Verstappen", "Lando Norris", "Charles Leclerc"]

def test_ranking_todos(campeonato):
    assert campeonato.ranking(20) == [
        "Max Verstappen",
        "Lando Norris",
        "Charles Leclerc",
        "Oscar Piastri",
        "Carlos Sainz",
        "George Russell",
        "Lewis Hamilton",
        "Oliver Bearman",
        "Franco Colapinto",
        "Liam Lawson",
        "Jack Doohan",
    ]

def test_ranking_no_modifica_orden_original(campeonato):
    campeonato.ranking(3)
    assert [piloto.numero for piloto in campeonato.pilotos] == [1, 4, 16, 81, 55, 63, 44, 38, 30, 43, 7]
