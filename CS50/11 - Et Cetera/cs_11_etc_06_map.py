# map służy wielokrotnemu wywoływaniu jakiejś funkcji
# dla każdego elementu zbioru, np. listy, tupla, setu, itd.


def main():

    # wywołujemy funkcję z 3 argumentami
    yell1("This", "is", "CS50")
    yell2("This", "is", "CS50")


# 1 Klasycznie. Funkcja przyjmuje dowolną ilość argumentów:


def yell1(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())

    # drukujemy argumentyy rozpakowane z listy uppercased:
    print("\n", *uppercased, "\n")


# 2 To samo z użyciem map:


def yell2(*words):
    uppercased = map(str.upper, words)

    # Tu uwaga: gdybyśmy napisali str.upper() z nawiasami, tobyśmy tę funkcję wywołali.
    # Chcemy ją tylko przekazać do funkcji map, dlatego pomijamy nawias.
    print("\n", *uppercased, "\n")


if __name__ == "__main__":
    main()
