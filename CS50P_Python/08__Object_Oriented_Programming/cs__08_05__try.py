# Robimy sprawdzenie inputów. Dopisujemy to nie w funkcji, a w klasie.
# Tym sposobem wszystko, co dotyczy klasy, jest razem.
# Jeśli jakaś inna funkcja stworzy obiekt, klasa zagwarantuje jego poprawność.


class Student:
    def __init__(self, name, house):

        # jeśli user nie poda imienia (if name == none)
        if not name:

            raise ValueError("\nError: missing name")
            # wywołujemy wyjątek z komunikatem, który powie programiście, co się stało.

            # Taki error można ładnie obsłużyć, dodając w metodzie get_student()
            # try: return Student(name, house)
            # except Value: ...

            # Alternatywy dla zgłoszenia błędu?
            # -print - to zły pomysł, bo uszkodzony obiekt Student już istnieje w pamięci.
            # -return None - też zły, bo zostawi uszkodzony obiekt i nic nie powie.
            # -sys.exit("missing name") - to zły pomysł, bo ubije program.

        if house not in ["Gryffindor", "Hufflepuff", "Slytherin", "Ravenclaw"]:

            raise ValueError("\nError: missing house")

        self.name = name
        self.house = house


def main():

    print()
    student = get_student()
    print(f"\n{student.name} is from {student.house}\n")


def get_student():

    name = input("Name: ")
    house = input("House: ")

    # tu dopisujemy try: i except:
    return Student(name, house)


if __name__ == "__main__":
    main()
