# poprzedni kod ze słownikiem w miejsce tupli
# słownik jest bardziej czytelny przy dłuższych programach.


def main():
    student = get_student()
    print(f"\n{student['name']} is from {student['house']}\n")


def get_student():
    print()

    # student = {}
    # student["name"] = input("Name: ")
    # student["house"] = input("House: ")
    # return student

    # krócej:
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}


if __name__ == "__main__":
    main()
