# generowanie dużych zbiorów liczb. Return vs yield.

# Na filmie pokazany jest przykład drukowania 1 znaku w 1 linijce,
# 2 znaków w 2 linijce, itd. Najpierw zapisano to bezpośrednio w main.

# Jednak lepiej kod pokapsułkować w funkcje, które są przenośne i dają się testować.
# Zrobiono to tak, że funkcja ładowała pustą listę [] znakami.
# Pierwszy argument listy, jeden znak, drugi argument dwa znaki, itd.
# Main drukował tylko każdy argument w kolejnej linijce.

# Tak napisany program był pokapsułkowany, ale przy dużej licznie, rzędu miliona,
# zawieszał się. Nie był w stanie wygenerować jednorazowo tak dużej listy,
# z której main mógłby drukować.

# Problemem było użycie słowa "return" które zwraca wartość, ale opuszcza funkcję.
# To dlatego ładowaliśmy jedną dużą listę, by ją zwrócić raz.

# Rozwiązanie to słowo "yield", które zwraca wartość i kontynuuje działanie pętli w funkcji.


def main():
    n = int(input("What's n? "))

    # drukuj po kolei każdy wiersz zwrócony przez funkcję:
    for s in sheep(n):
        print(s)


def sheep(n):
    for i in range(n):
        # tu wcześniej dodawaliśmy argumenty do wielkiej listy,
        # teraz zwracamy po jednym:
        yield "🐑" * i


if __name__ == "__main__":
    main()
