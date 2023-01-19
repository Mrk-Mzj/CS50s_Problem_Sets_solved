# Rozwijamy klasę o nową, własną metodę "charm". Będzie ona reagować na patronusy, jakie poda użytkownik.


class Student:
    def __init__(self, name, house, patronus):

        if not name:
            raise ValueError("\nError: missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Slytherin", "Ravenclaw"]:
            raise ValueError("\nError: missing house")
        self.name = name
        self.house = house
        self.patronus = patronus


    # Nasza własna metoda, którą wywołujemy z kodu:
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


    # Przy okazji dodajemy też metodę __str__, która uruchomi się, gdy kod spróbuje 
    # potraktować studenta, jako string (np. print(student))
    def __str__(self):
        return f"\nSo, you are that {self.name} from {self.house}! Do you like {self.patronus}?"


def main():

    print()
    student = get_student()
    print(student)              # tu próbujemy użyć obiekt 'student', jako string
    print(student.charm())      # tu wywołujemy naszą własną metodę .charm


def get_student():

    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()
