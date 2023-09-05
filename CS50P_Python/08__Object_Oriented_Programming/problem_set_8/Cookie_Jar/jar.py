# https://cs50.harvard.edu/python/2022/psets/8/jar/
# add and remove cookies from cookie jar object


class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        else:
            self.capacity = capacity
            self.size = 0

    def __str__(self):
        # return number of cookies to print
        if self.size == 0:
            return "💀"
        else:
            return self.size * "🍪"

    def deposit(self, n):
        # add n cookies (if adding them does not exceed capacity)
        if self.size + n > self.capacity:
            raise ValueError("Cannot deposit more than capacity")
        elif n < 0:
            raise ValueError("Cannot deposit a negative numer")
        else:
            self.size += n

    def withdraw(self, n):
        # remove n cookies (if doing so does not exceed quantity in the jar)
        if self.size - n < 0:
            raise ValueError("Cannot withdraw more than is in the jar")
        elif n < 0:
            raise ValueError("Cannot withdraw a negative numer")
        else:
            self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size


def main():
    jar = Jar()
    print(jar)

    jar.deposit(4)
    print(jar)

    jar.withdraw(2)
    print(jar)


if __name__ == "__main__":
    main()
