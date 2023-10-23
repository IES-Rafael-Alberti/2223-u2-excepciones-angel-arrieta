import pytest
from src.Ej_3_3 import example


@pytest.mark.parametrize(
    "inEjemplo, outMensaje",
    [
        ("Prueba1", "Salida"),
    ]
)


def test_example(inEjemplo, outMensaje):
    assert example(inEjemplo) == outMensaje
