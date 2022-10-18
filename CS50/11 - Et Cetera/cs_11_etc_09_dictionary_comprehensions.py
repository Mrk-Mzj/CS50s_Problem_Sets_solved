# zmieńmy listę (z samymi imonami) na listę słowników (z imionami i domami)
# odtwarzając tym samym strukturę z poprzednich plików

uczniowie = ["Hermiona", "Harry", "Ron"]

# 1 - Klasycznie:

gryffindorzanie = []
for student in uczniowie:
    gryffindorzanie.append({"name": student, "house": "Gryffindor"})
print("#1\n", gryffindorzanie, "\n")


# 2 - To samo, ale z list comprehension:

gryffindorzanie = [{"name": student, "house": "Gryffindor"} for student in uczniowie]
print("#2\n", gryffindorzanie, "\n")


# 3 - Podobnie, ale z Dictionary Comprehensions. Tym razem stworzymy słownik o strukturze
# {imie:Gryffindor, imie2:Gryffindor, imie3:Gryffindor}

gryffindorzanie = {student: "Gryffindor" for student in uczniowie}
print("#3\n", gryffindorzanie, "\n")
