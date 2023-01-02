def main():

    student = get_student()
    print(f"{student[0]} is from {student[1]}")

    # alternatywnie: rozpakowywanie tupla do dwóch zmiennych:
    # name, house = get_student()
    # print(f"{name} is from {house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house
    # Python nie zwraca tu dwóch zmiennych. Zwraca jedną, typu tuple.
    # Przypomina listę, ale jest niezmienna, niemutowalna.
    # To zaleta, jeśli chcemy mieć pewność, że my lub inny programista
    # przypadkowo nie zmienimy sobie tych wartości.

    # Jeśli jednak chcemy zwrócić edytowalną listę: return [name, house]


if __name__ == "__main__":
    main()
