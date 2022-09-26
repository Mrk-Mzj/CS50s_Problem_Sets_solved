# rozpiszmy w szczegółach to, co w poprzednim programie zrobiliśmy na skróty


class Student:

    # __init__ to funkcja, którą zawsze wywołuje konstruktor obiektu.
    # Przyjmuje obiekt, który właśnie powstaje, i parametry.

    # Parametry opisuję dla czytelności jako name i name_inputed,
    # ale tak naprawdę wszędzie może być to samo "name".

    def __init__(self, name_inputed, house_inputed):

        # Przypisujemy atrybuty (zmienne instancji) do obiektu.
        # Zasilamy pusty dotąd obiekt parametrami
        self.name = name_inputed
        self.house = house_inputed


def main():
    student = get_student()
    print(f"\n{student.name} is from {student.house}\n")


def get_student():
    print()

    # Poprzednio:

    # student = Student()
    # student.name = input("Name: ")
    # student.house = input("House: ")

    name_inputed = input("Name: ")
    house_inputed = input("House: ")
    student = Student(name_inputed, house_inputed)

    # Po nowemu jest czytelniej, bo przypisania przenieśliśmy do klasy.
    # Dodatkowo ten zapis pozwala skorzystać z metod klasy,
    # np. sprawdzających poprawność wprowadzonych danych.

    # BTW: Student(name, house) nazywamy wywołeniem konstruktora (constructor call)
    # Ten kon skonstruuje dla nas obiekt.

    return student


if __name__ == "__main__":
    main()
