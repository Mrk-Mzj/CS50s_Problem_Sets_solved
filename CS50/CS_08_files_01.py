name = input("What's your name? ")

# otwórz (utwórz jeśli nie istnieje) plik. Parametr "w" nadpisuje, "a" dodaje
file = open("CS_08_files_01_text.txt", "w")

# wpisz w plik zmienną
file.write(f"{name}\n")

# zapisz i zamknij plik
file.close
