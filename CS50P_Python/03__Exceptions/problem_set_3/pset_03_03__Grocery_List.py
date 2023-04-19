# Tworzymy listę zakupów.
# Pytamy o zakup. Jeśli jest już na liście, zwiększamy liczbę sztuk o 1.
# Po wciśnięciu Ctrl+Z (znacznik końca linii) wypisz listę zakupów
# wielkimi liniami, w kolejności alfabetycznej, z podaną ilością sztuk.


grocery = {}
count = 0

while True:
    try:
        item = input("Add to the list: (Ctrl+Z to finish) ")

        try:
            # spróbujmy wczytać do zmiennej count, ile sztuk mamy już na liście
            count = grocery[item.upper()]

        except KeyError:  # jeśli na liście nie było takiej pozycji, wpiszmy: 1
            grocery[item.upper()] = 1
            pass

        else:  # jeśli udało się wczytać (pozycja była na liście), zwiększamy liczbę o 1:
            grocery[item.upper()] = count + 1

    except EOFError:  # po wciśnięciu Ctrl+Z
        break


# sortujemy alfabetycznie:
grocery_sorted = {}
for _ in sorted(grocery):
    grocery_sorted[_] = grocery[_]

# drukujemy:
for _ in grocery_sorted:
    print(f"\n{_}: {grocery_sorted.get(_)}")
