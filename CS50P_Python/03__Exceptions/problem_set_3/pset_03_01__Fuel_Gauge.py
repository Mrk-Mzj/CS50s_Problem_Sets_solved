# Zasymulujmy działanie wskaźnika paliwa. User podaje dwie liczby. Przeliczamy je na procenty.
# Jeśli są spoza zakresu albo wywołuja błędy każemy mu je poprawić.
# Jeśli wynik jest blisko zera lub blisko 100% piszemy E lub F.

while True:
    try:
        fraction = input("Fraction? (X/Y)\n")

        x = int(fraction.split("/")[0])
        y = int(fraction.split("/")[1])

        percentage = round(100 * x / y)

        if percentage > 100:
            print("\nX must be less than Y.\n")

        else:
            # Input nie wywołał błędów i mieści się w zakresie,
            # kończymy program i wyskakujemy z pętli while:
            if percentage <= 1:
                percentage = "E"

            elif percentage >= 99:
                percentage = "F"

            print(f"{x}/{y} = {percentage} %")
            break

    except ValueError:
        print("\nYou have to input two integers in X/Y format.\n")
        pass

    except IndexError:
        print("\nYou have to input two integers in X/Y format.\n")
        pass

    except ZeroDivisionError:
        print("\nY must not be 0!\n")
        pass
