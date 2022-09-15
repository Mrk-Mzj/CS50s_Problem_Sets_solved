
# lista
list = ['Hermiona', 'Harry', 'Ron']

# miałknij dla każdego elementu tej listy
# a) 
count = 0
for student in range(len(list)):
    print ('Meaow a)', list[count])
    count += 1
print()


# b) bez countera; student jest integerem
for student in range(len(list)):
    print ('Meaow b)', list[student])
print()


# c) najkrócej; student jest stringiem
for student in list:
    print ('Meaow c)', student)
print()
