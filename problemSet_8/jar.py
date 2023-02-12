class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Negative cookies in Jar")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        if self.size > 0:
            return self.size * "🍪"
        else:
            return f"Jar is empty"

    def deposit(self, n):
        if n > self.capacity - self.size:
            raise ValueError("Too much 🍪")
        else:
            self._size += n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError("Not Enough 🍪")
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


# jar = Jar()
# print(jar)
# jar.deposit(10)
# print(jar)
# jar.withdraw(9)
# print(jar)
