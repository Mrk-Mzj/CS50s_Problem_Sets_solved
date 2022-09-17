#
# otwórzmy plik i sczytajmy zawartość:
# readlines() to funkcja Pythona z biblioteki I/O
with open("CS_08_files_02.txt", "r") as file:
    lines = file.readlines()


# Nasz plik tekstowy ma w sobie znaczniki końca linii. Print też dodaje znacznik końca linii.
# Możemy wczytywać kolejne linijki i skorzystać z ich \n:
for element in lines:
    print("a -", element, end="")

# albo lepiej: wyczyścić \n z wczytywanych linijek i dodawać je funkcją print()
for element in lines:
    print("b -", element.rstrip())


# Możemy to zoptymalizować.
# Dotąd czytaliśmy linię po linii, wpisaliśmy w listę, drukowaliśmy linię po linii.
# Możemy czytać po linii i od razu ją drukować:
with open("CS_08_files_02.txt", "r") as file:
    for element in file:
        print("c -", element.rstrip())
