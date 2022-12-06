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

while True:

    date_inputed = input("Input date as 5/25/1955 or May 25, 1955\n")

    # zapisujemy metodą 1:
    date_cached = date_inputed.split("/")

    # jeśli sczytaliśmy 3 elementy: sukces, wyskakujemy z pętli
    if len(date_cached) == 3:

        break

    # jeśli nie: porażka. Zczytujemy metodą 2:
    else:

        date_cached = date_inputed.split(" ")

        # przyjmuję, że numer dnia został podany zgodnie z instrukcją
        # i zapisał się z przecinkiem; czyszczę przecinek:

        try:
            date_cached[1] = date_cached[1].replace(",", "")

            # jeśli metoda zwróciła 3 elementy, skonwertuj miesiąc na liczbę i wyskocz z pętli
            if len(date_cached) == 3:

                try:
                    # konwersja: numer miesiąca to pozycja na liście months + 1:
                    date_cached[0] = str(months.index(date_cached[0]) + 1)
                    break

                except:
                    pass

        # jeśli nie istnieje 2 element
        except IndexError:
            pass


# W tym momencie mamy zmienną przechowującą dokładnie 3 elementy. Nie wiemy jeszcze czy prawidłowe.

# TODO: sprawdzenie czy elementy są liczbami i czy z przedziałów.
# Można napisać funkcję przyjmującą parametry - przedziały. Jeśli zwróci False, uruchamiamy od nowa odpytywanie usera.

# Sortowanie daty we właściwej kolejności:
date_ISO = []
date_ISO.append(date_cached[1])
date_ISO.append(date_cached[0])
date_ISO.append(date_cached[2])

print(date_ISO)
