from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x: object):
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self):
        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0

    def get_node(self, i: int) -> Node:
        if i < 0 or i > self.n: # Precondition
            return None
        if i < self.n / 2:
            p = self.dummy.next # head, i = 0
            for i in range(i):
                p = p.next
        else:
            p = self.dummy
            for i in range(self.n - 1):
                p = p.prev
        return p # i-th node

    def get(self, i) -> object:
        if i < 0 or i >= self.n: # Precondition
            raise Exception()
        return self.get_node(i).x # Return the i-th node

    def set(self, i: int, x: object) -> object:
        if i < 0 or i >= self.n:
            raise Exception()
        u = self.get_node(i) # i-th node
        y = u.x # Data from the i-th node
        u.x = x # Updating / overwriting data
        return y

    def add_before(self, w: Node, x: object) -> Node:
        if w == None:
            return Exception()
        u = self.Node(x)    # Step 1
        u.prev = w.prev     # Step 2
        u.next = w          # Step 2
        w.prev = u          # Step 3
        u.prev.next = u     # Step 4
        self.n += 1
        return u

    def add(self, i: int, x: object):
        if i < 0 or i > self.n: # Precondition
            return Exception()
        return self.add_before(self.get_node(i), x)

    def _remove(self, w: Node):
        if i < 0 or i >= self.n: # Precondition
            raise IndexError()
        w = self.get_node(i)
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1
        return w.x

    def remove(self, i: int):
        if i < 0 or i > self.n:  raise IndexError()
        return self._remove(self.get_node(i))

    def size(self) -> int:
        return self.n

    def append(self, x: object):
        self.add(self.n, x)

    def isPalindrome(self) -> bool:
        # todo
        pass

    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x
