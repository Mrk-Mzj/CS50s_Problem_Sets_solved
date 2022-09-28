# Jedziemy dalej. Usuwam customową metodę charm i patronus.

# Okazuje się, że deweloper może gdzieś w kodzie wpisać np. student.house="xyz"
# i nieświadomie ominąć funkcje sprawdzania poprawności z klasy.

# Zadeklarujmy więc w klasie metody, które przechwycą próby bezpośredniego odczytania
# lub zapisu zmiennej. Będzie to getter i setter. Sprawdzanie błędów umieścimy w ich środku.

# Aby oznaczyć getter użyjemy funkcji @property, a dla settera @house.setter.
# Będą one dekorować, rozszerzać funkcjonalność stojących przy nich metody.


class Student:
    def __init__(self, nnname, hhhouse):

        if not nnname:
            raise ValueError("\nError: missing name\n")

        self.name = nnname
        # Nie mamy settera dla 'name'. To jest więc zwykłe przypisanie,
        # które można nadpisać spoza klasy z pominięciem testu.

        self.house = hhhouse
        # Mamy setter dla 'house'. Choć wygląda identycznie, ta linijka wywołuje setter.
        # Getter i setter nadpisują działanie tej linijki. Jeśli oba usunąć, ta linia zadziała klasycznie.

    def __str__(self):
        return f"\nSo, you are that {self.name} from {self.house}!\n"

    # GETTER:
    @property
    def house(self):

        return self._house
        # Używamy tu _house z podkreśleniem. Nie można mieć tej samej nazwy house dla zmiennej instancji
        # i jednocześnie dla funkcji. To kolizja. Funkcja wywoływałaby samą siebie.
        # Dlatego standardowo używa się podkreślenia przed nazwą zmiennej.

    # SETTER:
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Slytherin", "Ravenclaw"]:
            raise ValueError("\nError: wrong house\n")

        self._house = house
        # Tak samo tu - używamy podkreślenia, aby funkcja nie wywoływała samej siebie.


def main():

    print()
    student = get_student()
    print(student)

    # Przyjmijmy, że to dopisał inny deweloper:

    student.house = "Hufflepuff"
    print(student)

    # Zaletą settera jest fakt, że deweloper może pisać, jakby klasycznie ustawiał wartość zmiennej
    # podczas gdy faktycznie jego polecenie przechodzi przez setter i zawarte w nim mechanizmy sprawdzające.
    # Setter sprawdzi zarówno input od użytkownika, jak i wywołania z kodu; wszystko.


def get_student():

    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
