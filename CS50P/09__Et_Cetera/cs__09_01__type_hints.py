# Python jest językiem dynamicznie typowanym. Nie deklaruje się typu zmiennej z góry.
# To może prowadzić do błędów. Np. kiedy user wpisuje cyfrę jako input, ta cyfra jest nadal typu STR.
# W wyłapywaniu błędów pomoże nam program mypy:
#
# PIP install mypy
# cd "11 - Et Cetera"
# mypy cs_11_etc_01_type_hints.py
#
# Podpowiadamy mu jakie typy danych są spodziewane (dajemy type hint), np n: int, number: int
# Uszczelniamy w ten sposób kod. Program przebadany mypy będzie miał mniej bugów.


def meow(n: int):
    for _ in range(n):
        print("meow!")


number: int = input("How many meaows? ")
meow(number)

# oczywiście błąd wskazany przez mypy naprawiamy pisząc = int(input(...))


# Spróbujmy obsłużyć inny błąd. Dajmy znać mypy że funkcja nie zwraca niczego: -> None
# Wówczas będzie mógł wyłapać miejsca, w których próbujemy użyć wartości zwracanej przez tę funkcję.


def meow2(n: int) -> None:
    for _ in range(n):
        print("meow!")


number2: int = int(input("How many meaows? "))
meows2: str = meow2(number2)
print(meows2)

# Naprawiamy to pozwalając zwrócić funkcji string do wydrukowania.
# To dobre podejście ze względu na testy jednostkowe. Testy lubią funkcje, które coś zwracają.
# Nie lubią fukcji które mają tylko działanie (side effects).
# Zmieniamy też type hint z -> None na -> str


def meow3(n: int) -> str:
    return "Meow!\n" * n


number3: int = int(input("How many meaows? "))
meows3: str = meow3(number3)
print(meows3)
