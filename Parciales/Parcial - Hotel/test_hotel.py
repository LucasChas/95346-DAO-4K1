"""Tests del parcial Hotel.
Uso:
    pytest test_hotel.py -v
"""

import sys
from pathlib import Path

import pytest

CARPETA = Path(__file__).resolve().parent
if str(CARPETA) not in sys.path:
    sys.path.insert(0, str(CARPETA))

ARCHIVO = str(CARPETA / "reservas.csv")

from reserva import Reserva  # noqa: E402
from estandar import Estandar  # noqa: E402
from suite import Suite  # noqa: E402
from cabana import Cabana  # noqa: E402
from hotel import Hotel  # noqa: E402


@pytest.fixture
def hotel():
    return Hotel(ARCHIVO)


# ---------------------------------------------------------------------------
# Constructor / carga del archivo
# ---------------------------------------------------------------------------

def test_constructor_hotel(hotel):
    assert hotel is not None
    assert len(hotel.reservas) == 8

def test_constructor_archivo_inexistente():
    with pytest.raises(FileNotFoundError):
        Hotel("archivo_inexistente.csv")

def test_orden_de_carga(hotel):
    codigos = [reserva.codigo for reserva in hotel.reservas]
    assert codigos == ["E101", "E102", "E103", "S201", "S202", "C301", "C302", "C303"]

def test_tipos_numericos_cargados(hotel):
    primera = hotel.reservas[0]
    assert primera.precio_noche == 8000
    assert primera.noches == 3
    assert isinstance(primera.noches, int)
    suite = hotel.reservas[3]
    assert suite.servicios_spa == 3
    assert isinstance(suite.servicios_spa, int)


# ---------------------------------------------------------------------------
# Herencia y composición
# ---------------------------------------------------------------------------

def test_herencia_reservas():
    assert issubclass(Estandar, Reserva)
    assert issubclass(Suite, Reserva)
    assert issubclass(Cabana, Reserva)

def test_reserva_es_abstracta():
    with pytest.raises(TypeError):
        Reserva(1, "X000", "Nadie", 1000, 1)

def test_composicion_hotel_reservas(hotel):
    assert hasattr(hotel, "reservas")
    for reserva in hotel.reservas:
        assert isinstance(reserva, Reserva)

def test_clases_segun_tipo(hotel):
    for reserva in hotel.reservas:
        if reserva.tipo == 1:
            assert isinstance(reserva, Estandar)
        elif reserva.tipo == 2:
            assert isinstance(reserva, Suite)
        else:
            assert isinstance(reserva, Cabana)


# ---------------------------------------------------------------------------
# Atributos
# ---------------------------------------------------------------------------

def test_atributos_estandar():
    estandar = Estandar("E101", "Laura Gomez", 8000, 3, "si")
    assert estandar.tipo == 1
    assert estandar.codigo == "E101"
    assert estandar.huesped == "Laura Gomez"
    assert estandar.precio_noche == 8000
    assert estandar.noches == 3
    assert estandar.desayuno == "si"

def test_atributos_suite():
    suite = Suite("S201", "Carlos Pereyra", 25000, 2, 3)
    assert suite.tipo == 2
    assert suite.servicios_spa == 3

def test_atributos_cabana():
    cabana = Cabana("C301", "Diego Fernandez", 15000, 5, "si")
    assert cabana.tipo == 3
    assert cabana.mascota == "si"

def test_str_incluye_codigo():
    assert "E101" in str(Estandar("E101", "Laura Gomez", 8000, 3, "si"))
    assert "S201" in str(Suite("S201", "Carlos Pereyra", 25000, 2, 3))
    assert "C301" in str(Cabana("C301", "Diego Fernandez", 15000, 5, "si"))


# ---------------------------------------------------------------------------
# calcular_costo de cada tipo
# ---------------------------------------------------------------------------

def test_estandar_con_desayuno_sin_descuento():
    # 8000 * 3 + 1500 * 3
    assert Estandar("E101", "Laura Gomez", 8000, 3, "si").calcular_costo() == pytest.approx(28500)

def test_estandar_sin_desayuno_con_descuento():
    # 7000 * 10 = 70000 -> -15%
    assert Estandar("E102", "Martin Diaz", 7000, 10, "no").calcular_costo() == pytest.approx(59500)

def test_estandar_con_desayuno_con_descuento():
    # (9000 * 8 + 1500 * 8) = 84000 -> -15%
    assert Estandar("E103", "Sofia Ruiz", 9000, 8, "si").calcular_costo() == pytest.approx(71400)

def test_estandar_7_noches_no_tiene_descuento():
    assert Estandar("E999", "Borde", 1000, 7, "no").calcular_costo() == pytest.approx(7000)

def test_suite_con_spa():
    # 25000 * 2 + 4000 * 3
    assert Suite("S201", "Carlos Pereyra", 25000, 2, 3).calcular_costo() == pytest.approx(62000)

def test_suite_sin_spa():
    assert Suite("S202", "Valentina Sosa", 30000, 4, 0).calcular_costo() == pytest.approx(120000)

def test_cabana_con_mascota():
    # (15000 * 5 + 3000) = 78000 -> +20%
    assert Cabana("C301", "Diego Fernandez", 15000, 5, "si").calcular_costo() == pytest.approx(93600)

def test_cabana_sin_mascota():
    # 12000 * 2 + 3000
    assert Cabana("C302", "Julieta Morales", 12000, 2, "no").calcular_costo() == pytest.approx(27000)


# ---------------------------------------------------------------------------
# Funcionalidades de Hotel
# ---------------------------------------------------------------------------

def test_calcular_promedio_noches(hotel):
    # 41 noches / 8 reservas = 5.125 -> 5
    promedio = hotel.calcular_promedio_noches()
    assert promedio == 5
    assert isinstance(promedio, int)

def test_obtener_reserva_mayor_costo(hotel):
    reserva = hotel.obtener_reserva_mayor_costo()
    assert reserva.codigo == "C303"
    assert reserva.huesped == "Pablo Castro"
    assert reserva.calcular_costo() == pytest.approx(154800)

def test_calcular_recaudacion_total(hotel):
    assert hotel.calcular_recaudacion_total() == pytest.approx(616800)

def test_contar_estandar_con_descuento(hotel):
    assert hotel.contar_estandar_con_descuento() == 2

def test_contar_cabanas_con_mascota(hotel):
    assert hotel.contar_cabanas_con_mascota() == 2

def test_cantidad_por_tipo(hotel):
    assert hotel.cantidad_por_tipo() == {"Estándar": 3, "Suite": 2, "Cabaña": 3}

def test_buscar_reserva_existente(hotel):
    reserva = hotel.buscar_reserva("S202")
    assert reserva is not None
    assert reserva.huesped == "Valentina Sosa"
    assert isinstance(reserva, Suite)

def test_buscar_reserva_inexistente(hotel):
    assert hotel.buscar_reserva("Z999") is None

def test_codigos_por_rango_costo(hotel):
    assert hotel.codigos_por_rango_costo(50000, 100000) == ["E102", "E103", "S201", "C301"]

def test_codigos_por_rango_costo_inclusive(hotel):
    assert hotel.codigos_por_rango_costo(27000, 28500) == ["E101", "C302"]

def test_codigos_por_rango_costo_vacio(hotel):
    assert hotel.codigos_por_rango_costo(200000, 300000) == []
