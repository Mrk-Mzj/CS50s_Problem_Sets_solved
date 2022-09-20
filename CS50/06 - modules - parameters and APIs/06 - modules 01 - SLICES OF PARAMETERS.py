# uruchamiamy pisząc w konsoli:
"""
python '06 - modules 01 - SLICES OF PARAMETERS.py' imie1 imie2 imie3
"""


# importujemy moduł, który umożliwi uruchamianie programu z parametrem
import sys

# sys.argv to ciąg parametrów, pośród których pierwszy to zawsze nazwa programu, a dopiero drugi pochodzi od użytkownika
if len(sys.argv) == 1:

    # opuść program załączając komunikat o błędzie
    sys.exit("Too few arguments")

# dla każdego elementu, z przedziału [1 : nieskończoność] (czyli tzw. slice) drukuj...
for name in sys.argv[1:]:
    print("Hello, my name is", name)


# ciekawostka: zapis [1:-1] to przedział od drugiego do przedostatniego elementu
