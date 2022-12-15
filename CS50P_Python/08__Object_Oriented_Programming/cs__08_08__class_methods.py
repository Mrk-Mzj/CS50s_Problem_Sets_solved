# Napiszmy klasę, która odpowiada na pytanie, do jakiego domu powinien
# trafić uczeń Hogwartu. Użyjemy metody klasy - nie metody obiektu - czyli
# metody wspólnej dla każdego obiektu, nie różnicującej ich.

# Najpierw napiszmy to klasycznie, tworząc obiekt tiara:

import random


class Tiara:
    def __init__(self):
        # tworzymy zmienną instancji
        self.houses = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]

    def przydziel(self, name):
        print(f"{name} is in {random.choice(self.houses)}")


tiara = Tiara()
tiara.przydziel("Harry")
