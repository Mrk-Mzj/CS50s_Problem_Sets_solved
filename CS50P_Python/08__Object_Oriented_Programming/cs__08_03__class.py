# w miejsce podstawowych typów danych utwórzmy swój własny.
# Definiujemy go przy pomocy klasy, czyli szablonu, wzoru. Nazywamy ją z wielkiej litery:


class Student:
    ...


def main():

    print()
    student = get_student()
    print(f"\n{student.name} is from {student.house}\n")  # type: ignore
    # dodaję linijkę ignore. Zmienne name i house są podkreślane jako nieznane,
    # ale program działa prawidłowo


def get_student():

    # tworzymy obiekt 'student' czyli instancję klasy 'Student'
    # tworzymy atrybuty klasy (a właściwie zmienne instancji) 'name' i 'house'

    student = Student()
    student.name = input("Name: ")  # type: ignore
    student.house = input("House: ")  # type: ignore

    return student


if __name__ == "__main__":
    main()
