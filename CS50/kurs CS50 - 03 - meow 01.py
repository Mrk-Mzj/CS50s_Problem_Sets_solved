
# różne sposoby na zapisanie tego samego:

#1
i=0
while i<3:
    print('#1 meow while')
    i+=1

#2
for _ in range(3):          # znak _ jest często używany w licznikach, ale można użyć też i 
    print('#2 meow for')
 
#3   
print('#3 meow times \n' *3)


#######################################


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

