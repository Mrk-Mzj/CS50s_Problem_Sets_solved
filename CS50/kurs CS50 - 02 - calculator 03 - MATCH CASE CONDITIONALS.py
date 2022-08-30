
def main():

    # asking and assigning a float value to variables
    x = float(input("What's X? "))
    y = float(input("What's Y? "))
    operation = input('What to do? ( + - * / ) ')

    # calculations
    match operation:
        case '+':
            result = cleaned(x+y)
        case '-':
            result = cleaned(x-y)
        case '*':
            result = cleaned(x*y)
        case '/':
            result = cleaned(x/y)
        case _:
            result = "wrong, because it was not an operation!"

    # printing the result
    print(f'\n Result is: {result} \n')



def cleaned(dirt):
      
    #convering to string (f''), separating tousands with commas(:,), replacing commas with spaces, cleaning '.0'
    return (f'{dirt:,}').replace(',' , ' ').replace('.0' , '')
    

main()

