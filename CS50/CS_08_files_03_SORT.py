#
# Chcemy wczytać plik i wypisać imiona w kolejności alfabetycznej.
# Tworzę listę do której za chwilę załaduję kolejne linie tekstu:
names = []

# Ładuję names kolejnymi linijkami
# przy wczytywaniu nie trzeba używać "r"
with open("CS_08_files_02.txt") as file:
    for element in file:
        names.append(element.rstrip())

# Sortuję elementy i drukuję je
for name in sorted(names):
    print(f"Hello, {name}")


# Mogę to skrócić i posortować od razu cały plik:
with open("CS_08_files_02.txt") as file:
    for element in sorted(file):
        print(f"Witaj, {element.rstrip()}")
