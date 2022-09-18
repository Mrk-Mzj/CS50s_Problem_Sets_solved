# Sortowanie danych z pliku CSV.
#
studenci = []

with open("cs_08_files_04.csv") as file:
    for linia in file:
        # dzielimy linię na zmienne; dodajemy je do słownika opisującego ucznia; dodajemy go do listy studentów
        imie, szkola = linia.rstrip().split(",")
        uczen = {"imie": imie, "szkola": szkola}
        studenci.append(uczen)


# aby posortować listę studentów po imionach, trzeba pobrać imię każdego ucznia z jego słownika.
# Piszemy funkcję, która zwraca imię.
def klucz(uczen):
    return uczen["imie"]


# Funkcja sorted() używa naszej funkcji klucz() by zbudować sobie listę imion i posortować dane wg niej
for uczen in sorted(studenci, key=klucz):
    print(uczen["imie"], "uczy się w", uczen["szkola"])

print()

# Ale nie musimy defioniować funkcji klucz. Można to samo skrócić do zapisu z tzw. funkcją lambda.
# Jest to funkcja bez nazwy. Od razu piszemy, co przyjmuje i co ma zwracać:
for uczen in sorted(studenci, key=lambda uczen: uczen["imie"]):
    print(uczen["imie"], "uczy się LAMBDA w", uczen["szkola"])
