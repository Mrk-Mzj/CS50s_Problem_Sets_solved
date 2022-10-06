uniwersytety = [
    "Bercley",
    "Cambridge",
    "Harvard",
    "MIT",
    "Oxford",
    "Princeton",
    "Sorbonne",
    "Stanford",
    "Yale",
]

for _ in uniwersytety:
    print(_)

szukany = input("\nKtórego szukamy?\n")


# 1 - szukanie po kolei (algorytm liniowy):
pozycja = uniwersytety.index(szukany) + 1
print(f"\nJest na {pozycja} miejscu.\n")

# + mierzenie czasu


# 2 - szukanie przy pomocy dzielenia na połowy (alg. binarny):
# + mierzenie czasu
