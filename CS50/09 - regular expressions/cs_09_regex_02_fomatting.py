# formatowanie
# Przyjmijmy, że user wprowadza "Nazwisko, Imię" zamiast "Imię Nazwisko".
# Chcemy to wyczyścić.

import re

name = input("What's your name? ").strip()

# 1 pierwotny, też poprawny kod:

if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"


# posłużmy się regex. Okazuje się, że funkcja re.search, którą znamy,
# umożliwia użycie nawiasu do grupowania danych

# szukamy wzoru "abc, def" (działa też przy braku lub nadmiarze spacji)
matches = re.search(r"^(.+), *(.+)$", name)

# 2 jeśli taki wzór istnieje, przypisz jego części do zmiennych:
if matches:
    last, first = matches.groups()
    name = f"{first} {last}"

# 3 można nawet krócej. Drobna uwaga: grupy liczymy od 1, nie od 0:
if matches:
    name = matches.group(2) + " " + matches.group(1)

# 4 można nawet wciągnąć deklarację matches do if - trzeba tylko specjalnie oznaczyć :=
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)

print(f"Hello {name}")
