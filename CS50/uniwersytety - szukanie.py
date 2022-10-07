def main():

    uniwersytety = [
        "Bercley",
        "California",
        "Cambridge",
        "Chicago",
        "Columbia",
        "Harvard",
        "MIT",
        "Oxford",
        "Pennsylvania",
        "Princeton",
        "Sorbonne",
        "Stanford",
        "Yale",
    ]

    print("\n", uniwersytety)
    szukany = input("\nKtórego szukamy?\n")
    print()

    # 0 - metoda index
    miejsce = uniwersytety.index(szukany) + 1
    print(f"#0 Jest na {miejsce} miejscu.")

    # 1 - szukanie po kolei (algorytm liniowy):
    miejsce = 1
    for _ in uniwersytety:
        if _ == szukany:
            print(f"#1 Jest na {miejsce} miejscu.")
            break
        miejsce += 1

    # 2 - szukanie przy pomocy dzielenia na połowy (algorytm binarny):
    # Zmierz długość listy. Podziel na pół. Zaokrąglij do int.
    # !Round zaokrągla do liczb parzystych, unikając kumulowania się błędów zaokrągleń.

    miejsce = 0
    while len(uniwersytety) > 1:
        miejsce = srodek_listy(uniwersytety, miejsce)

        # Porównaj środkowy element listy z szukanym:
        # - jeśli środkowy == szukany, wypisz jego lokalizację
        if uniwersytety[miejsce] == szukany:
            print(f"#2 Znalazłem {szukany}!")
            break

        # - jeśli środkowy > szukany, skróć listę do pierwszej połowy
        elif uniwersytety[miejsce] > szukany:
            print(f"#2 {szukany} jest w pierwszej części listy:")
            uniwersytety = uniwersytety[0:miejsce]
            print(uniwersytety)

        # - jeśli środkowy < szukany, skróć listę do drugiej połowy
        else:
            print(f"#2 {szukany} jest w drugiej części listy:")
            uniwersytety = uniwersytety[miejsce + 1 : len(uniwersytety)]
            print(uniwersytety)

    # + mierzenie czasu
    print()


def srodek_listy(uniwersytety, miejsce):
    miejsce = round(len(uniwersytety) / 2)
    print(f"\n#2 Środek jest w {uniwersytety[miejsce]}")
    return miejsce


if __name__ == "__main__":
    main()
