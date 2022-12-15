# w miejsce podstawowych typów danych utwórzmy swój własny.
# Definiujemy go przy pomocy klasy, czyli szablonu, wzoru. Nazywamy ją z wielkiej litery:


class Student:
    ...


def main():

    print()
    student = get_student()
    print(f"\n{student.name} is from {student.house}\n")


def get_student():

    # tworzymy obiekt 'student' czyli instancję klasy 'Student'
    # tworzymy atrybuty klasy (a właściwie zmienne instancji) 'name' i 'house'

    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")

    return student


if __name__ == "__main__":
    main()
