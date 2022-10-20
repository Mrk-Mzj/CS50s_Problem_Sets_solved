# test jednostkowy B - z użyciem ASSERT
from cs__05_01__program import square


def main():

    test_square()


# metoda testowania ręcznie z użyciem ASSERT; krótka ale mało przydatna,
# bo nie wypisuje szczegółów testu, wywala nieobsłużony błąd i nie testuje dalej
def test_square():

    assert square(5) == 25
    assert square(0) == 0
    assert square(-2) == 4


if __name__ == "__main__":
    main()
