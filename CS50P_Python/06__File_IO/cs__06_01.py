name = input("What's your name? ")

# otwórz plik (lub utwórz, jeśli nie istnieje).
# Parametr "w" nadpisuje, "a" dodaje do pliku
file = open("cs__06_01.txt", "w")

# wpisz w plik zmienną
file.write(f"{name}\n")

# zapisz i zamknij plik
file.close
