from doctest import OutputChecker


def main():
    name = input("What's your name? ")
    # sklejanie mógłbym robić klasycznie w main, ale przenoszę je do wydzielonej funkcji hello_maker
    # która ma input i output, a tym samym daje się łatwo testować
    # Gdyby sklejanie robić wewnątrz nawiasu print(), wyjściem były napis na ekranie, a nie testowalna zmienna
    print(hello_maker(name))


# wartość domyślna: world
def hello_maker(name="world"):
    return f"Hello, {name}"


if __name__ == "__main__":
    main()
