from calculadora import Sumar, Restar, Multiplicar, Dividir
import pytest


def test_sumar_failed():
    assert Sumar(2, 3) == 10


def test_restar_failed():
    assert Restar(8, 3) == 10


def test_multiplicar_failed():
    assert Multiplicar(2, 5) == 20


def test_dividir_failed():
    assert Dividir(10, 2) == 8


def test_dividir_cero_failed():
    assert Dividir(5, 0) == 0