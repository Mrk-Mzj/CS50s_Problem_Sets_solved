# Zapisywanie danych do CSV;
# posłużymy się znów słownikiem

# Harry Number Four, Privet Drive
# Ron The Burrow
# Draco Malfoy Manor

import csv

imie = input("Jak masz na imię? ")
mieszkanie = input("Gdzie mieszkasz? ")


with open("cs__06_09.csv", "a", newline="") as file:
    # fieldnames służy opisaniu kolejności kolumn w dokumencie
    # dzięki temu dane w writerow mogą być wpisane w dowolnej kolejności

    writer = csv.DictWriter(file, fieldnames=["imie", "mieszkanie"])
    writer.writerow({"imie": imie, "mieszkanie": mieszkanie})
