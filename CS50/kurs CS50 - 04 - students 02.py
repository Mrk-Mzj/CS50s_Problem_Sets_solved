
# słownik
dictionary = {
    'Hermiona': 'Gryffindor', 
    'Harry':    'Gryffindor', 
    'Ron':      'Gryffindor',
    'Draco':    'Slytherin'
}


# drukowanie pojedynczej pary klucz-wartość
print (f'\n','Draco należy do', dictionary['Draco'], '\n')


# drukowanie wszytskich par klucz-wartość
for address in dictionary:
    print (address,'należy do',dictionary[address])

