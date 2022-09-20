# Sortowanie danych z CVS z nagłówkami

import csv

studenci = []
with open("cs_08_files_08.csv") as file:

    # Wadą poprzedniego kodu była mała elastyczność. 
    # Kod zakładał, że pierwsza kolumna to zawsze imię a druga to zawsze mieszkanie.
    # Jeśli zewnętrzny program zmieni kolejność kolumn w pliku CSV, lub coś doda, tamten kod się wysypie.

    # Przenieśmy więc nazwy kolumn do pliku CSV i użyjmy funkcji DictReader.
    # Teraz każda linia jest wczytywana nie jako lista[0], a jako słownik["imie"].
    # Można zmienić kolejność kolumn w CSV, a nawet dodać nowe. 
    # DictReader poszuka wśród nich kolumn o wpisanej w kodzie nazwie.

    czytnik = csv.DictReader(file)

    for linia in czytnik:
        studenci.append({"imie": linia["imie"], "mieszkanie": linia["mieszkanie"]})

for uczen in sorted(studenci, key=lambda uczen: uczen["imie"]):
    print(uczen["imie"], "mieszka w", uczen["mieszkanie"])

print()

