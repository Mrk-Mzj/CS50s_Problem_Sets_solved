# test jednostkowy C - z użyciem ASSERT i przechwytywaniem błędów
from cs__05_01__program import square


def main():

    test_square()


# metoda testowania ręcznie z użyciem ASSERT i przechwytywaniem błędów
# jeszcze więcej pisania, niż z IF
def test_square():

    try:
        assert square(5) == 25
    except AssertionError:
        print(f"ERROR: 5 squared was {square(5)} instead of 25")

    try:
        assert square(0) == 0
    except AssertionError:
        print(f"ERROR: 0 squared was {square(0)} instead of 0")

    try:
        assert square(-2) == 4
    except AssertionError:
        print(f"ERROR: -2 squared was {square(-2)} instead of 4")

    else:
        print("SUCCESS!")


if __name__ == "__main__":
    main()
