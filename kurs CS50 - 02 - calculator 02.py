
def main():

    # asking and assigning a float value to variables
    x = float(input("What's X? "))
    y = float(input("What's Y? "))

    adding(x,y)


def adding(x,y):
    
    # separating large numbers with commas and replacing them with spaces
    print(f'Adding result is: { (x+y) :,}'.replace(',' , ' '))


main()

