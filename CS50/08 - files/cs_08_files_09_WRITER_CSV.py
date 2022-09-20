# Zapisywanie danych do CSV;
# pusty CSV na dysku ma na początku tylko jedną linijkę "imie,mieszkanie" i wciśnięty enter

# Harry Number Four, Privet Drive
# Ron The Burrow
# Draco Malfoy Manor

import csv

imie = input("Jak masz na imię? ")
mieszkanie = input("Gdzie mieszkasz? ")


with open("cs_08_files_09.csv", "a", newline="") as file:
    # open domyślnie dodaje newline;
    # wyłączam to żeby nie mieć podwójnych enterów od writerow

    writer = csv.writer(file)
    writer.writerow([imie, mieszkanie])
