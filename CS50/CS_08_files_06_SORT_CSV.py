# Sortowanie danych z pliku CSV.
#
studenci = []

with open("CS_08_files_04.csv") as file:
    for linia in file:
        # dzielimy linię na zmienne; dodajemy je do słownika opisującego ucznia; dodajemy go do listy studentów
        imie, szkola = linia.rstrip().split(",")
        uczen = {"imie": imie, "szkola": szkola}
        studenci.append(uczen)


# aby posortować listę studentów po imionach, trzeba pobrać imię każdego ucznia z jego słownika.
# Piszemy funkcję, która zwraca imię.
def klucz(uczen):
    return uczen["imie"]


# Funkcja sorted() używa naszej funkcji by zbudować sobie listę imion i posortować dane wg niej
for uczen in sorted(studenci, key=klucz):
    print(uczen["imie"], "uczy się w", uczen["szkola"])
