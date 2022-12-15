# test jednostkowy A - z użyciem IF
from cs__05_01__program import square


def main():

    test_square()


# metoda testowania ręcznie z użyciem IF; strasznie dużo pisania
def test_square():

    if square(5) != 25:
        print(f"ERROR: 5 squared was {square(5)} instead of 25")

    elif square(0) != 0:
        print(f"ERROR: 0 squared was {square(0)} instead of 0")

    elif square(-2) != 4:
        print(f"ERROR: -2 squared was {square(-2)} instead of 4")

    else:
        print("SUCCESS!")


if __name__ == "__main__":
    main()
