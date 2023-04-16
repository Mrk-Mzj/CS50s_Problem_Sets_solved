# słownik, czyli zbiór par {'klucz':'wartość'}
# dictionary = {'Hermiona':'Gryffindor', 'Harry':'Gryffindor', 'Ron':'Gryffindor', 'Draco':'Slytherin'}

dictionary = {
    "Hermiona": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}


# drukowanie pojedynczej pary klucz-wartość
print("\n", "Draco należy do", dictionary["Draco"], "\n")


# drukowanie wszytskich par klucz-wartość
for address in dictionary:
    print(address, "należy do", dictionary[address])

print()
