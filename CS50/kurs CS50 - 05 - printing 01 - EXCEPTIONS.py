

# odpytujmy usera w nieskończoność, dopóki nie poda prawidłowej odpowiedzi

while True:
    try:
        x = int(input("What's x? "))
        print(f'X is {x}')
        break
    
    # w przypadku błędnej wartości piszemy ostrzeżenie i pętla rusza od nowa
    
    # wypisujemy tu konkretny typ błędu, jaki może zrobić user (ValueError)
    # brak dokładnej deklaracji jest dopuszczalny, ale to zła praktyka; może utrudnić debugowanie
    
    except ValueError:
        print('X is not an integer! \n')


print('End \n')

