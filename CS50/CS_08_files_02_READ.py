#
# otwórzmy plik i sczytajmy zawartość:
# readlines() to funkcja Pythona z biblioteki I/O
with open("CS_08_files_02.txt", "r") as plik:
    imiona = plik.readlines()


# Nasz plik tekstowy ma w sobie znaczniki końca linii. Print też dodaje znacznik końca linii.
# Możemy wczytywać kolejne linijki i skorzystać z ich \n:
for linia in imiona:
    print("a -", linia, end="")

# albo lepiej: wyczyścić \n z wczytywanych linijek i dodawać je funkcją print()
for linia in imiona:
    print("b -", linia.rstrip())


# Możemy to zoptymalizować.
# Dotąd czytaliśmy linię po linii, wpisaliśmy w listę, drukowaliśmy linię po linii.
# Czyli dwókrotnie skanowaliśmy wszystkie linie.
# Możemy czytać po linii i od razu ją drukować:

with open("CS_08_files_02.txt", "r") as plik:
    for linia in plik:
        print("c -", linia.rstrip())

# BTW: przy wczytywaniu nie trzeba używać parametru "r"