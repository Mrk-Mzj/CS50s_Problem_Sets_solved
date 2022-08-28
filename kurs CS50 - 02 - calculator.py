
def adding(x,y):
    
     # printing with separating large numbers with commas
    print(f'Adding result is: { (x+y) :,}')

    # same with spaces instead of commas
    print(f'Adding result is: { (x+y) :,}'.replace(',' , ' '))

# CODE
# assigning a float value to variables
x = float(input("What's X? "))
y = float(input("What's Y? "))

adding(x,y)

