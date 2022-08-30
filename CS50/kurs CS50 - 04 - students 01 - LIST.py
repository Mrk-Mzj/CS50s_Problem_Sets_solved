
# lista
list = ['Hermiona', 'Harry', 'Ron']

# miałknij dla każdego elementu tej listy
# a) 
count = 0
for student in range(len(list)):
    print(f'Meaow a) {list[count]}')
    count += 1


# b) bez countera; student jest integerem
for student in range(len(list)):
    print(f'Meaow b) {list[student]}')


# c) najkrócej; student jest stringiem
for student in list:
    print(f'Meaow c) {student}')

