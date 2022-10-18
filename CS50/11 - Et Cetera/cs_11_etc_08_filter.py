# filtrowanie z użyciem funkcji filter

uczniowie = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

# Funkcja, którą użyjemy do sprawdzania;
# Ten zapis to odpowiednik if (...) return True


def czy_gryffindor(student):
    return student["house"] == "Gryffindor"


# użycie funkcji filter przypomina mocno użycie map(),
# gdy dwa pliki wcześniej pisaliśmy: uppercased = map(str.upper, words).
# Tu również przekazujemy funkcję bez nawiasów, które by ją uruchamiały.

gryffindorzanie = filter(czy_gryffindor, uczniowie)

for gryf in gryffindorzanie:
    print(gryf["name"])

print()
# zapis sortowany robi się z funkcją Lambda:

gryffindorzanie = filter(czy_gryffindor, uczniowie)

for gryf2 in sorted(gryffindorzanie, key=lambda student: student["name"]):
    print(gryf2["name"])
