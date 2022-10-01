# Wracamy do programu ze studentami (07_getter_setter.py)
# i upraszczamy go, dla zwiększenia czytelności.
# Skorzystajmy z metod klasy, żeby przenieść
# funkcjonalność get_student() do wnętrza klasy. To dobra praktyka, by mieć to razem.


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"\nSo, you are that {self.name} from {self.house}!\n"

    # Metoda klasy ma tę zaletę, że można jej użyć przed utworzeniem obiektu.
    # Najpierw wywołujemy get(), zdobywamy dane studenta i dopiero tworzymy obiekt student.
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():

    print()
    student = Student.get()
    print(student)


"""
student = get_student()

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
"""


if __name__ == "__main__":
    main()
