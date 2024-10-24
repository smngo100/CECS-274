import numpy as np
from Interfaces import Queue


class ArrayQueue(Queue):
    def __init__(self):
        self.n = 0  # Number of elements in the queue
        self.j = 0  # Index of the first element
        self.a = self.new_array(1)  # Initialize an array a of size 1

    def new_array(self, n: int) -> np.array:
        return np.zeros(n, object)

    def resize(self):
        '''
            Resize the array
        '''
        b = self.new_array(max(1, 2 * self.n))  # Step 1
        for k in range(0, self.n):  # Step 2
            b[k] = self.a[(self.j + k) % len(self.a)]
        self.a = b  # Step 3
        self.j = 0  # Step 4

    def add(self, x: object):
        '''
            shift all j > i one position to the right
            and add element x in position i
        '''
        if self.n == len(self.a):  # Precondition, invariant
            self.resize()
        self.a[(self.j + self.n) % len(self.a)] = x  # Step 1
        self.n += 1  # Step 2, increment n by 1
        return True

    def remove(self) -> object:
        '''
            remove the first element in the queue
        '''
        if self.n <= 0:  # Precondition
            raise IndexError()
        x = self.a[self.j % len(self.a)]  # Step 1
        self.j = (self.j + 1) % len(self.a)  # Step 2
        self.n -= 1  # Step 3, decrement n by 1
        if len(self.a) > 3 * self.n:  # Invariant
            self.resize()
        return x  # Step 4

    def size(self):
        return self.n

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i < self.n - 1:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator += 1
        else:
            raise StopIteration()
        return x