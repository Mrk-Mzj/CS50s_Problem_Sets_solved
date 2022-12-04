# Odpytuj usera o pozycje z menu. Pokazuj mu rosnącą sumę.
# Podsumuj gdy wciśnie Ctrl+Z (znak końca linii w Windows).

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}
order = []
sum = 0

while True:
    try:
        item = input("What do you want, sir? (Ctrl+Z to finish) ")
        sum += menu[item]
        order.append(item)
        print("$", sum)

    except EOFError:  # po wciśnięciu Ctrl+Z
        break

    except KeyError:  # w przypadku pozycji spoza menu
        pass

print("\nYour order:")
for _ in order:
    print(_)

print("Check: $", sum)
