# Rozwijamy klasę o customowową metodę charm do rzucania patronusa.
# Przy okazji dodajemy też metodę __str__ która pozwala potraktować studenta, jak STR


class Student:
    def __init__(self, name, house, patronus):

        if not name:
            raise ValueError("\nError: missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Slytherin", "Ravenclaw"]:
            raise ValueError("\nError: missing house")
        self.name = name
        self.house = house
        self.patronus = patronus

    # Side quest:
    def __str__(self):
        return f"\nSo, you are that {self.name} from {self.house}! Do you like {self.patronus}s?\n"

    # Customowa metoda:
    def charm(self):
        match self.patronus:

            case "aaa":
                return "Student is casting mighty patronus AAA!\n"
                # równie dobrze można tu robić print, a w main wywołać samo student.charm()
            case "bbb":
                return "Student is casting mighty patronus BBB!\n"
            case "ccc":
                return "Student is casting mighty patronus CCC!\n"
            case _:
                return "Student is you have no power here\n"


def main():

    print()
    student = get_student()
    print(student)  # tu próbujemy użyć obiekt, jakby był STR
    print(student.charm())  # a tu korzystamy z customowej metody


def get_student():

    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()
