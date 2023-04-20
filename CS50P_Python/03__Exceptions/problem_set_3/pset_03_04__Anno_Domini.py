# Przyjmij datę w formacie 9/8/1636 lub September 8, 1636.
# Skonwertuj i wydrukuj w formacie DD-MM-YYYY. Obsłuż błędy.

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
    # wczytaj dane
    input = read_input()

    # jeśli wczytane dane są prawidłowe, posortuj je i wydrukuj
    if check(input) == True:
        print(sort(input))

    else:
        main()


def read_input():
    # zwraca listę z dokładnie trzema elementami, które powinny być liczbami. Czy są - to sprawdzi osobna funkcja.

    while True:
        date_inputed = input("Input date as 5/25/1955 or May 25, 1955\n")

        # Załóżmy, że data zapisana jest w formacie 5/25/1955.
        # Spróbujmy podzielić wczytaną zmienną w miejscu "/":
        date = date_inputed.split("/")

        # jeśli wyciągnęliśmy dokładnie 3 elementy, wyskakujemy z pętli
        # i przechodzimy do sprawdzenia danych:
        if len(date) == 3:
            return date

        else:
            # Jeśli nie wyciągnęliśmy 3 elementów zakładamy,
            # że data zapisana jest w formacie 'May 25, 1955'.
            # Spróbujmy więc podzielić wczytaną zmienną w miejscu " ":
            date = date_inputed.split(" ")

            # Jeśli wyciągnęliśmy dokładnie 3 elementy...
            if len(date) == 3:
                # usuńmy przecinek po numerze dnia
                date[1] = date[1].replace(",", "")

                # i spróbujmy skonwertować nazwę miesiąca, zapisaną słownie, na liczbę.
                # Liczba to pozycja na liście miesięcy + 1.
                # Konwertuję ją na str, by pasowała do date_cached - która zawiera stringi.
                try:
                    date[0] = str(months.index(date[0]) + 1)
                    return date

                except:
                    pass


def check(input):
    # Sprawdza czy elementy są liczbami całkowitymi i czy z właściwych przedziałów.
    # Zwraca True dla poprawnych liczb, i False dla błędu.

    try:
        if (
            (1 <= int(input[0]) <= 12)  # miesiąc
            and (1 <= int(input[1]) <= 31)  # dzień
            and (0 <= int(input[2]) <= 2222)  # rok
        ):
            return True

        else:
            return False

    except ValueError:
        return False


def sort(input):
    # Sortowanie daty we właściwej kolejności:
    date_sorted = []
    date_sorted.append(input[1])
    date_sorted.append(input[0])
    date_sorted.append(input[2])

    return date_sorted


if __name__ == "__main__":
    main()
