# Przeciążanie operatorów to zmiana ich działania.
# Np. + w przypadku stringów jest przeciążony i służy łączeniu tekstów.

# Stwórzmy skrytkę bankową, w której różne osoby mogą trzymać pieniądze w 3 różnych walutach


class Vault:
    def __init__(self, dollars=0, euros=0, pounds=0):
        self.dollars = dollars
        self.euros = euros
        self.pounds = pounds

    def __str__(self):
        return (
            f"\n{self.dollars} dollars, {self.euros} euros and {self.pounds} pounds.\n"
        )

    # tu przeciążamy operator dodawania:
    def __add__(self, other):
        dollars = self.dollars + other.dollars
        euros = self.euros + other.euros
        pounds = self.pounds + other.pounds
        return Vault(dollars, euros, pounds)
        # return dollars, euros, pounds - to zwracałoby tupla, ale nie innicjowało obiektu Vault


print()

harry = Vault(100, 50, 25)
print("Harry has:", harry)

ron = Vault(25, 50, 100)
print("Ron has:", ron)

# Robimy zrzutkę. Chcemy połączyć ich konta. Klasycznie wygląda to tak:

# dollars = harry.dollars + ron.dollars
# ...
# zrzutka = Vault(dollars, euros, pounds)
# print(zrzutka)

# Dużo pisana przy każdym wywołaniu. Możemy jednak przeciążyć operator
# i wywoływać tę funkcję krótko:

zrzutka = harry + ron
print("Sum:", zrzutka)
