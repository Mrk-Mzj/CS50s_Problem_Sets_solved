

def main():
    times = how_many_times()
    print ('meaow \n'*times)



def how_many_times():
    # odpytuj dopóki nie dostaniesz poprawnej liczby miałknięć
    while True:
        # zaokrąglij liczby po przecinku
        n = round(float(input('How many times to meaow? ')))
        if n>0: 
            return n


main()


