# Przyjmij datę w formacie 9/8/1636 lub September 8, 1636.
# Skonwertuj i wydrukuj w formacie YYYY-MM-DD. Obsłuż błędy.

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    # date_cached = read_input()

    # W tym momencie mamy zmienną przechowującą dokładnie 3 elementy. Nie wiemy jeszcze czy prawidłowe.
    # TODO: sprawdzenie czy elementy są liczbami i czy z przedziałów.
    # Można napisać funkcję przyjmującą parametry - przedziały. Jeśli zwróci False, uruchamiamy od nowa odpytywanie usera.

    # date_sorted = sort(read_input())
    date_iso = check(sort(read_input()))

    # ten zapis eliminuje drukowanie None. Kiedy mogłoby się zdarzyć?
    # Gdy występuje błąd w check() funkcja main() jest wywoływana ponownie, do skutku. Robi się rekurencja.
    # Po otrzymaniu wlaściwej daty drukuje się data i None dla każdego z błędów. Ta linia temu zapobiega.
    if date_iso:
        print(date_iso)


def read_input():
    # zwraca listę z dokładnie trzema elementami, które powinny być liczbami. Czy są - to sprawdzi osobna funkcja.

    while True:
        date_inputed = input("Input date as 5/25/1955 or May 25, 1955\n")

        # Załóżmy, że data zapisana jest w formacie 5/25/1955.
        # Spróbujmy podzielić wczytaną zmienną w miejscu "/":
        date_cached = date_inputed.split("/")

        # jeśli wyciągnęliśmy dokładnie 3 elementy, wyskakujemy z pętli
        # i przechodzimy do sprawdzenia danych:
        if len(date_cached) == 3:
            return date_cached

        else:
            # Jeśli nie wyciągnęliśmy 3 elementów zakładamy,
            # że data zapisana jest w formacie 'May 25, 1955'.
            # Spróbujmy więc podzielić wczytaną zmienną w miejscu " ":
            date_cached = date_inputed.split(" ")

            # Jeśli wyciągnęliśmy dokładnie 3 elementy...
            if len(date_cached) == 3:
                # usuńmy przecinek po numerze dnia
                date_cached[1] = date_cached[1].replace(",", "")

                # i spróbujmy skonwertować nazwę miesiąca, zapisaną słownie, na liczbę.
                # Liczba to pozycja na liście miesięcy + 1.
                # Konwertuję ją na str, by pasowała do date_cached - która zawiera stringi.
                try:
                    date_cached[0] = str(months.index(date_cached[0]) + 1)
                    return date_cached

                except:
                    pass


def sort(date_cached):
    # Sortowanie daty we właściwej kolejności:
    date_sorted = []
    date_sorted.append(date_cached[1])
    date_sorted.append(date_cached[0])
    date_sorted.append(date_cached[2])

    return date_sorted


def check(date_sorted):
    # sprawdza czy elementy są liczbami i czy z przedziałów.
    # jeśli nie, odpytaj ponownie:

    try:
        if (
            (1 <= int(date_sorted[0]) <= 31)
            and (1 <= int(date_sorted[1]) <= 12)
            and (0 <= int(date_sorted[2]) <= 2222)
        ):
            return date_sorted
        else:
            main()

    except ValueError:
        main()


if __name__ == "__main__":
    main()
