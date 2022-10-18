# drukowanie zawartości listy z jednoczesnym numerowaniem pozycji

uczniowie = ["Hermiona", "Harry", "Ron"]


# 1 - Klasycznie:

for i in range(len(uczniowie)):
    print(i + 1, uczniowie[i])

print()

# 2 - Enumerate. Przechodzi przez daną sekwencję i zwraca nie tylko
# odczytaną wartość, ale i pozycję. Dla każdego elementu udziela dwóch odpowiedzi.

for i, student in enumerate(uczniowie):
    print(i + 1, student)

print()
