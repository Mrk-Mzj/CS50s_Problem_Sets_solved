# program, którego funkcje będziemy testować
# specyficzna nazwa, bo przy imporcie niedozwolone są: spacje, myślniki i cyfra na początku nazwy
# w porządku są: podkreślenia i cyfry wewnątrz nazwy


def main():
    x = int(input("What's x? "))
    print("x squared is:", square(x))


def square(n):
    return n * n


# ten zapis sprawia, że test jednostkowy nie odpali funkcji main
if __name__ == "__main__":
    main()
