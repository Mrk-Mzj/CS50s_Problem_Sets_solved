# poprzedni kod zamieniamy na bardziej elastczną funkcję

def main():
    # wywołujemy funkcję z parametrem. W ten sposób funkcja może być wywoływana z wielu miejsc w kodzie, za każdym razem z innym pytaniem
    number = get_int("What's x? ")
    print(f'X is {number} \n')


def get_int(prompt):
    while True:
        try:
            # return użyty w tym miejscu pozwala uniknąć inicjowania zmiennej x i stosowania zapisu else
            return int(input(prompt))

        except ValueError:
            # pass stosujemy, kiedy zauważamy błąd, ale nie chcemy nic z nim robić. Tu, dzięki pętli, pozwala zwyczajnie powrócić do pytania o x.
            pass


main()

