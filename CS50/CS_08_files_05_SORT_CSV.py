# Sortowanie danych z pliku CSV.
#
# Tworzymy listę studentów. Każdy element listy to zbiór danych o studencie. Odpowiednik pojedynczego wiersza w pliku CSV.
# Do każdego wiersza trzeba wstawić kolumny. Pary informacji imie:abc, szkola:xyz... Czyli słownik.
# Dzięki temu będziemy mogli posortować po wybranej kolumnie, a nie po pierwszym wyrazie w danej linii.

studenci = []

with open("CS_08_files_04.csv") as file:
    for linia in file:

        imie, szkola = linia.rstrip().split(",")

        # każdy uczeń dostaje swój własny słownik, odpowiednik kolumn:
        uczen = {}
        uczen["imie"] = imie
        uczen["szkola"] = szkola

        # alternatywny zapis:
        # uczen = {"imie": imie, "szkola": szkola}

        # gotowy słownik opisujący ucznia dodajemy do listy studentów
        studenci.append(uczen)


for uczen in studenci:
    print(uczen["imie"], "uczy się w", uczen["szkola"])


