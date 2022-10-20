# Przekazywanie zmiennej liczby argumentów do funkcji

# args to argumenty pozycyjne, zależne od miejsca. Jak w listach
# rozpakowywanych do funkcji (patrz: poprzedni plik).

# kwargs (keyword args) to argumenty słów kluczowych. Jak w słownikach.


# Napiszmy funkcję która przyjmuje zmienną liczbę argumentów pozycyjnych
# i argumentów słów kluczowych:


def f(*args, **kwargs):
    print()
    print("Positional:", args)
    print("Named:", kwargs)
    print()


f(100, 50, 25)  # positional args; tuple
f(dollars=100, euros=50, plns=25)  # named kwargs; dict
f(100, 50, plns=25)  # both

# Funkcja może rozpakować otrzymane tuple z args i słowniki z kwargs,
# dzięki gwiazdce:

#    print("Positional:", *args)
#    print("Named:", *kwargs)
