# Pisanie dokumentacji opiera się na konwencjach. Piszemy przy pomocy
# komentarzy blokowych, wewnątrz funkcji, używając odpowiednich słów kluczowych.
# Dzięki stosowaniu konwencji możemy używać potem narędzi do automatycznego
# tworzenia dokumentacji.


def meow3(n: int) -> str:
    """
    Meow n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "Meow!\n" * n


number3: int = int(input("How many meaows? "))
meows3: str = meow3(number3)
print(meows3)
