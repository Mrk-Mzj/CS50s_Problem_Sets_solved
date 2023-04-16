# lista [ słowników {'kluczy':'wartości'} ]
# list_of_directories = [{'name':'Hermiona', 'house':'Gryffindor', 'patronus':'Otter'}, {'name':'Harry', 'house':'Gryffindor', 'patronus':'Stag'}, itd.]

list_of_dictionaries = [
    {"name": "Hermiona", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]


# drukowanie konkretnej wartości z listy słowników
print("\n", list_of_dictionaries[3]["name"], "\n")


# drukowanie kolumny z listy słowników
for wizard in list_of_dictionaries:
    print(wizard["name"])


print()
