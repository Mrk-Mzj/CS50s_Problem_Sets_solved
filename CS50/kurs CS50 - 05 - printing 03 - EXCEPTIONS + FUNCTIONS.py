def main():
    # wywołujemy funkcję z parametrem. W ten sposób funkcja może być wywoływana z wielu miejsc w kodzie, z innym pytaniem
    number = get_int("What's x? ")
    print(f'X is {number} \n')


def get_int(prompt):
    while True:
        try:
            # return użyty tu pozwala uniknąć inicjowania zmiennej x i stosowania zapisu else
            return int(input(prompt))

        except ValueError:
            # pass służy odmowie działania wobec zaistnienia błędu. Tu pozwala zwyczajnie powrócić do pytania o x.
            pass


main()

