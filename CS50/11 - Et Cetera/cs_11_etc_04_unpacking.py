# Rozpakowywanie wartości do kilku zmiennych

# 1, z użyciem listy:
# Zapis zmiennej *coins z gwiazdką rozpakowuje ją do poszczególnych wartości:


def total(dollars, euros, plns):
    return (dollars * 17 + euros) * 29 + plns


coins = [100, 50, 25]

print(total(*coins))


# 2, z użyciem słownika. Dwie gwiazdki sięgają po klucz i po wartość:

coins = {"dollars": 100, "euros": 50, "plns": 25}
print(total(**coins))

# Pojedyncza gwiazdka służy do sięgania po sam klucz:


def waluty(waluta1, waluta2, waluta3):
    print(f"waluty to {waluta1}, {waluta2}, {waluta3}\n")


waluty(*coins)
