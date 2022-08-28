
def main():

    # asking and assigning a float value to variables
    x = float(input("What's X? "))
    y = float(input("What's Y? "))

    # in case of adding
    result = cleaning(x+y)

    # printing the result
    print(f'\n Result is: {result} \n')



def cleaning(dirt):
      
    #convering to string (f''), separating tousands with commas(:,), replacing commas with spaces, cleaning '.0'
    return (f'{dirt:,}').replace(',' , ' ').replace('.0' , '')
    

main()

