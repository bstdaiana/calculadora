from calculadora import Sumar, Restar, Multiplicar, Dividir
import pytest

def test_sumar():
    assert Sumar(2, 3) == 5

def test_restar():
    assert Restar(5, 2) == 3

def test_multiplicar():
    assert Multiplicar(4, 3) == 12

def test_dividir():
    assert Dividir(10, 2) == 5

def test_dividir_cero():
    with pytest.raises(ZeroDivisionError):
        Dividir(5, 0)