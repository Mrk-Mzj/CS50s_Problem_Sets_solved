# Napiszmy program dla ucznia i nauczyciela z Hogwartu.
# Obaj są czarodziejami, więc będą mmiały część kodu wspólną.
# Tak nauczymy się dziedziczenia.


class Wizard:
    def __init__(self, name):
        # Niech Wizard służy zbieraniu nazwisk i sprawdzaniu błędów w nich,
        # a podklasy zajmą się danymi specyficznymi dla siebie.

        if not name:
            raise ValueError("No name given")
        self.name = name

    ...


class Student(Wizard):
    def __init__(self, name, house):

        # Korzystamy z metody init klasy nadrzędnej
        # (tzw. superclass), by uzyskać self.name:
        super().__init__(name)

        # Reszta kodu będzie specyficzna dla tej konkretnej podklasy:
        if not house:
            raise ValueError("No house given")
        self.house = house

    ...


class Professor(Wizard):
    def __init__(self, name, teaches):

        super().__init__(name)

        if not teaches:
            raise ValueError("No teaches given")
        self.teaches = teaches

    ...


student = Student("Draco", "Slytherin")
print(f"{student.name} is in {student.house}")
