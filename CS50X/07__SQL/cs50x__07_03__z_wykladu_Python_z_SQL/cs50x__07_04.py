# Stworzyliśmy db z pliku csv. Teraz możemy w nim szukać, np. popularnego filmu:

import csv
from cs50 import SQL

db = SQL("sqlite:///CS50X/07__SQL/cs50x__07_03__z_wykladu_Python_z_SQL/favorites.db")

title = input("Title: ").strip()
# np. The Office
# Tym razem nie musimy czyścić zapytania np. .upper(), ponieważ metoda LIKE,
# której zaraz użyjemy, ignoruje wielkość znaków.

rows = db.execute("SELECT COUNT(*) AS counter FROM shows WHERE title LIKE ?", title)
# COUNT zwraca liczbę rzędów, które pasują do kryteriów.
# AS oznacza alias, tymczasową, uproszczoną nazwę; tu: counter.

# Metoda execute z biblioteki cs50 w przypadku SELECT zwraca listę słowników.
# https://docs.cs50.net/2018/x/psets/7/finance/finance.html#hints
# W tym wypadku lista ma tylko jeden słownik:
# [{'counter': xx}]

row = rows[0]  # {'counter': xx}

print(row["counter"], "\n")  # xx
