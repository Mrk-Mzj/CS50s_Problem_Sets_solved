# Requirements:

# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “No periods, spaces, or punctuation marks are allowed.”
# “All vanity plates must start with at least two letters.”

# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”


def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")

    else:
        print("Invalid")


def is_valid(plate):
    # returns True if s meets all requirements

    # Wstęne sprawdzenie
    # czy zgadza się liczba znaków, wszystkie są alfanumeryczne a dwa pierwsze są literami:
    if 2 <= len(plate) <= 6 and plate.isalnum() and plate[:2].isalpha():

        # Jeśli nie ma żadnych cyfr, kończymy sprawdzanie sukcesem:
        if plate.isalpha():
            return True

        # Gdzieś są cyfry. Szukamy pierwszej.
        else:
            index = 0
            for p in plate:

                if p.isdigit():
                    # Kiedy ją znajdziemy, musi być różna od zera, a wszystkie znaki po niej też muszą być cyframi.
                    # Wtedy mamy sukces. Inaczej od razu ogłaszamy porażkę.

                    if p != "0" and plate[index:].isdigit():
                        return True
                    else:
                        return False

                index += 1

            # pierwsza cyfra była zerem lub blok cyfr nie sięgał do końca:
            return False

    # wstępne sprawdzenie się nie powiodło:
    else:
        return False


if __name__ == "__main__":
    main()
