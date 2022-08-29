
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