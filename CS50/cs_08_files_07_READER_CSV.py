# Sortowanie danych z bardziej złożonego pliku CSV.
#
# Czasem w pliku CSV pojawiają się dane, które same w sobie mają przecinek, jak adres mieszkania.
# Taki element można zapisać w cucdzysłowiu, ale dalsze pisanie obejścia ze .split(",") byłoby czasochłonne.
# Sprzątanie i rozdzielanie danych zostawiamy funkcji reader() z modułu CSV

import csv

studenci = []
with open("cs_08_files_07.csv") as file:

    czytnik = csv.reader(file)

    for imie, mieszkanie in czytnik:
        studenci.append({"imie": imie, "mieszkanie": mieszkanie})

    ### alternatywnie:

    for linia in czytnik:
        studenci.append({"imie": linia[0], "mieszkanie": linia[1]})

for uczen in sorted(studenci, key=lambda uczen: uczen["imie"]):
    print(uczen["imie"], "mieszka w", uczen["mieszkanie"])

print()

