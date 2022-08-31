
#testowanie zasięgu działania zmiennych (scope)

x=1
y=7
print(x)

def test():
    x=666
    print(x)
    print(y)

test()
print(x)


# rysowanie schodów malejących

for position in range(5):
    print('#'*position)

# rysowanie schodów rosnących
steps = 1
while steps < 5:
    print(' '*(5-steps),'#'*steps)
    steps += 1

