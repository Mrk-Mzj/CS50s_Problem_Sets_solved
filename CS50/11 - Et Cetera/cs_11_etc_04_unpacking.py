# Rozpakowywanie wartości do kilku zmiennych


def total(dollars, euros, plns):
    return (dollars * 17 + euros) * 29 + plns


coins = [100, 50, 25]

# zapis zmiennej z gwiazdką rozpakowuje ją do poszczególnych wartości:
print(total(*coins))
