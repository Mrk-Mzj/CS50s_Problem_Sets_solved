# Robimy sprawdzenie inputów. Dopisujemy to nie w funkcji, a w klasie.
# Tym sposobem wszystko, co dotyczy klasy, jest razem.
# Jeśli jakaś inna funkcja stworzy obiekt, klasa zagwarantuje jego poprawność.


class Student:
    def __init__(self, name_inputed, house_inputed):

        # jeśli user nie poda imienia (if name_inputed == none)
        if not name_inputed:

            raise ValueError("missing name")
            # wywołujemy wyjątek z komunikatem, który powie programiście, co się stało.

            # Taki error można ładnie obsłużyć, dodając w metodzie get_student()
            # try: return Student(name_inputed, house_inputed)
            # except Value: ...

            # Alternatywy dla zgłoszenia błędu?
            # -print - to zły pomysł, bo uszkodzony obiekt Student już istnieje w pamięci.
            # -return None - też zły, bo zostawi uszkodzony obiekt i nic nie powie.
            # -sys.exit("missing name") - to zły pomysł, bo ubije program.

        self.name = name_inputed
        self.house = house_inputed


def main():

    print()
    student = get_student()
    print(f"\n{student.name} is from {student.house}\n")


def get_student():

    name_inputed = input("Name: ")
    house_inputed = input("House: ")

    # tu dopisujemy try: i except:
    return Student(name_inputed, house_inputed)


if __name__ == "__main__":
    main()
