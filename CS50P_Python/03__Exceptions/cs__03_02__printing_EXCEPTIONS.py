
while True:

    # dobrą praktyką jest testowanie tylko jednej linii kodu; przenosimy więc print dalej
    try:
        x = int(input("What's x? "))
    
    # w przypadku błędu zrób to:
    except ValueError:
        print('X is not an integer! \n')
    
    # jeśli nie ma błędu i wszystko jest ok, kontynuuj z tym:
    else:
        print(f'X is {x}')
        break

# Zmienną x drukujemy koniecznie w else, a nie tu. 
# W przypadku błędu konwersji int, zmienna x nie zostaje zainicjowana. 
# Próba wydrukowania jej tu kończy się kolejnym błędem.

print('End \n')

