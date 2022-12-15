#
# sczytywanie zawartości pliku CSV, rozdzielanie par oddzielonych przecinkami
with open("cs__06_04.csv") as file:
    for linia in file:

        # sposób 1: tworzymy listę, do której pakujemy po 2 elementy
        row = linia.rstrip().split(",")
        print(row[0], "mieszka w", row[1])

        # sposób 2: przydzielamy elementom listy nazwy
        imie, szkola = linia.rstrip().split(",")
        print(imie, "mieszka w", szkola)
