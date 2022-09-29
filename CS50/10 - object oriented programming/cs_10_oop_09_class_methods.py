# Teraz napiszemy to tak, by nie dało się stworzyć wielu tiar przydziału.

import random


class Tiara:
    # tworzymy zmienną klasy. Jedną, wspólną dla wszystkich ewentualnych instancji.
    houses = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]

    # tworzymy metodę klasy. Nie przydzielamy już self, czyli obiektu,
    # a cls - referencję do klasy. Taka jest konwencja.
    @classmethod
    def przydziel(cls, name):
        print(f"{name} is in {random.choice(cls.houses)}")


# tiara = Tiara()
Tiara.przydziel("Harry")
