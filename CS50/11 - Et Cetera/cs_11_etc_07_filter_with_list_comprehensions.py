# zapis list comprehensions może być użyty równiez do filtrowania:

uczniowie = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

# do listy gryffindorzanie dodaj
gryffindorzanie = [
    # imię studenta
    # z listy uczniów,
    # jeśli jego dom to Gryffindor:
    student["name"]
    for student in uczniowie
    if student["house"] == "Gryffindor"
]

print()

# wypisz każdego gryffindorzanina:
for gryf in sorted(gryffindorzanie):
    print(gryf)

print()
