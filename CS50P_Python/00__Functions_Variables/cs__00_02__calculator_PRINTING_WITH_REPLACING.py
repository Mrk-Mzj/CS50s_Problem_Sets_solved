# Function prints adding result, formatted in two ways:
def print_adding(x, y):
    # ...separating large numbers with commas
    print(f"Adding result is: { (x+y) :,}")

    # ...separating with spaces instead of commas
    print(f"Adding result is: { (x+y) :,}".replace(",", " "))


# assigning float value to variables:
x = float(input("What's X? "))
y = float(input("What's Y? "))


# executing the function:
print_adding(x, y)
