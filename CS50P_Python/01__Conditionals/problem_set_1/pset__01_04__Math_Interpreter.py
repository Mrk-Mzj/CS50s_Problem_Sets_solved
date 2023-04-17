"""
implement a program that prompts the user for an arithmetic expression and then calculates 
and outputs the result as a floating-point value formatted to one decimal place. 
Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer

For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0
"""


txt = input("\nCalculate x ? y:\n")
math = txt.split(" ")  # zwraca listę 3 elementów w formacie [x,działanie,y]

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
