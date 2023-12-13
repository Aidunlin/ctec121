# jar.py
# Aidan Linerud


class Jar:
    def __init__(self, capacity=12):
        if capacity < 1:
            raise ValueError

        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n: int):
        if self._size + n > self._capacity:
            raise ValueError

        self._size += n

    def withdraw(self, n: int):
        if self._size - n < 0:
            raise ValueError

        self._size -= n

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def size(self) -> int:
        return self._size
