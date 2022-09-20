#
# Chcemy wczytać plik i wypisać imiona w kolejności alfabetycznej.
# Tworzę listę do której za chwilę załaduję kolejne linie tekstu:
imiona = []


# Ładuję 'imiona' kolejnymi linijkami. Obcinam im w locie znaczniki \n.

with open("cs_08_files_02.txt") as plik:
    for linia in plik:
        imiona.append(linia.rstrip())


# Sortuję elementy i drukuję je

for name in sorted(imiona):
    print(f"Hello, {name}")


# Mogę to skrócić i posortować od razu cały plik:

with open("cs_08_files_02.txt") as plik:
    for linia in sorted(plik):
        print(f"Witaj, {linia.rstrip()}")
