txt = input("\nCalculate x ? y:\n")
math = txt.split(" ")   # zwraca listę 3 elementów w formacie [x,działanie,y]

# sprawdzam czy user nie zapomniał o użyciu spacji:
if len(math) > 1:

    x = float(math[0])
    y = float(math[2])

    match math[1]:
        case "+":
            print(x + y)

        case "-":
            print(x - y)

        case "*":
            print(x * y)

        case "/":
            print(round((x / y), 1))
