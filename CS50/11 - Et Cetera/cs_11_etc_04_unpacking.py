# Rozpakowywanie wartości do kilku zmiennych



def total(dollars, euros, plns):
    return (dollars * 17 + euros) * 29 + plns

# 1, z użyciem listy:

coins1 = [100, 50, 25]
print(total(*coins1))

# Zapis zmiennej *coins z gwiazdką rozpakowuje ją do poszczególnych wartości.


# 2, z użyciem słownika.
# Dwie gwiazdki sięgają po klucz i po wartość:

coins2 = {"dollars": 100, "euros": 50, "plns": 25}
print(total(**coins2))

# Pojedyncza gwiazdka służy do sięgania po sam klucz:


def waluty(waluta1, waluta2, waluta3):
    print(f"Waluty to: {waluta1}, {waluta2}, {waluta3}\n")


waluty(*coins2)
