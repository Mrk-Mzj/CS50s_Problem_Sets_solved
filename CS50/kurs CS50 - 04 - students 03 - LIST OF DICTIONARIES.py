
# lista [ słowników {} ]
list_of_directories = [
    
    {'name': 'Hermiona', 'house': 'Gryffindor',   'patronus': 'Otter'},
    {'name': 'Harry',    'house': 'Gryffindor',   'patronus': 'Stag'},
    {'name': 'Ron',      'house': 'Gryffindor',   'patronus': 'Terrier'},
    {'name': 'Draco',    'house': 'Slytherin',    'patronus': None}
]


# drukowanie konkretnej wartości z listy słowników
print ('\n', list_of_directories[3]['name'],'\n')


# drukowanie kolumny z listy słowników
for czarodziej in list_of_directories:
    print (czarodziej['name'])


print()

