# test jednostkowy D - z użyciem ASSERT i PYTEST
# pip install -U pytest
# podczas instalacji może pojawić się napis, by ustawić w systemie zmienną środowiskową PATH
"""
pytest cs__05_05__test_D_PYTEST.py
"""
from cs__05_01__program import square


# metoda testowania ręcznie z użyciem ASSERT i testowana pakitem PYTEST
# bez funkcji main, bez warunków, chwytania błędów i printów
# niestety zatrzymuje realizację funkcji na pierwszym błędzie, dlatego piszemy kilka funkcji:


def test_square_positive():

    assert square(2) == 4
    assert square(3) == 9


def test_square_negative():

    assert square(-2) == 4
    assert square(-3) == 9


def test_square_neutral():

    assert square(0) == 0
