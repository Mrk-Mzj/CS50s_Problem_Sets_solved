# Odpytujmy usera w nieskończoność, dopóki nie poda integera. Wtedy break wyskoczy z pętli.
# W przypadku błędnej wartości piszemy ostrzeżenie i pętla rusza od nowa.

while True:
    try:
        x = int(input("What's x? "))
        print(f"X is {x}")
        break

    except ValueError:
        print("X is not an integer! \n")

    # wypisujemy tu konkretny typ błędu, jaki może zrobić user (ValueError)
    # brak dokładnej deklaracji jest dopuszczalny, ale to zła praktyka; może utrudnić debugowanie


print("End \n")
