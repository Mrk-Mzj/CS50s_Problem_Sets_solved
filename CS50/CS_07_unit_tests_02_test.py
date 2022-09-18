"""
pytest CS_07_unit_tests_02_test.py
"""
from cs_07_unit_tests_02_program import hello_maker

# ponownie rozbijam test na 2 funkcje, by łatwiej łapać bugi:


def test_default_hello_maker():
    assert hello_maker() == "Hello, world"


def test_argument_hello_maker():
    assert hello_maker("Marek") == "Hello, Marek"


# te dwa osobne testy mogę zapisać do dwóch osobnych plików. Oba pliki umieścić w folderze z testami.
# Jeśli folder z testami oznaczę (umieszczając w nim pusty plik o nazwie __init__.py)
# będę mógł użyć polecenia "pytest nazwa_folderu" i uruchomić wszystkie pliki z testami, które tam są.
