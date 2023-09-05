from datetime import date
import sys, inflect

# Program to tell how many minutes passed since the user was born.
# https://cs50.harvard.edu/python/2022/psets/8/seasons/
# pip install inflect


def main():
    birth = input("\nInput your birth date as 2000-02-22\n")
    birth = convert_str_to_date_object(birth)
    minutes = how_many_minutes_since(birth)

    # printing num comma separated
    print(f"\n{minutes:,}")

    # printing num converted to words:
    print(inflect.engine().number_to_words(minutes))



def convert_str_to_date_object(birth):
    # converts inputed date to Date object
    try:
        birth = date(int(birth[:4]), int(birth[5:7]), int(birth[8:]))

    except ValueError:
        sys.exit("\nError: invalid birth date")
    
    if birth >= date.today():
        sys.exit('\nError: invalid birth date')

    return birth



def how_many_minutes_since(birth_date):
    # calculate how many minutes passed

    # convert timedelta object to minutes, and round to int
    return round((date.today() - birth_date).total_seconds() / 60)



if __name__ == "__main__":
    main()
