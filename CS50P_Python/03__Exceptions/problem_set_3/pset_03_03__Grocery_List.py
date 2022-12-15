# Odpytuj pozycje do kupna. Po wciśnięciu Ctrl+Z (znacznik końca linii) wypisz
# wielkimi liniami, w kolejności alfabetycznej, z podaną ilością sztuk


grocery = {}
count = 0

while True:
    try:
        item = input("Add to the list: (Ctrl+Z to finish) ")

        try:
            count = grocery[item.upper()] + 1  # wczytujemy ile sztuk już zapisaliśmy

        except KeyError:  # jeśli na liście nie było takiej sztuki
            grocery[item.upper()] = 1
            pass

        else:  # była jakaś sztuka, kontynuujemy try tutaj:
            grocery[item.upper()] = count

    except EOFError:  # po wciśnięciu Ctrl+Z
        break


# sortowanie słownika po owocach:
grocery_sorted = {}
for _ in sorted(grocery):
    grocery_sorted[_] = grocery[_]

# drukowanie:
for _ in grocery_sorted:
    print(f"\n{_}: {grocery_sorted.get(_)}")
