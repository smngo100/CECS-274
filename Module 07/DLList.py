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
        if i < 0 or i > self.n:  # Precondition
            return None
        if i < self.n / 2:
            u = self.dummy.next  # head, i = 0
            for j in range(i):
                u = u.next
        else:
            u = self.dummy
            for j in range(self.n - i):
                u = u.prev
        return u  # i-th node

    def get(self, i) -> object:
        if i < 0 or i >= self.n:  # Precondition
            raise Exception()
        return self.get_node(i).x  # Return the i-th node

    def set(self, i: int, x: object) -> object:
        if i < 0 or i >= self.n:
            raise Exception()
        u = self.get_node(i)  # i-th node
        y = u.x  # Data from the i-th node
        u.x = x  # Updating / overwriting data
        return y

    def add_before(self, w: Node, x: object) -> Node:
        if w == None:
            return Exception()
        u = self.Node(x)  # Step 1
        u.prev = w.prev  # Step 2
        u.next = w  # Step 2
        w.prev = u  # Step 3
        u.prev.next = u  # Step 4
        self.n += 1
        return u

    def add(self, i: int, x: object):
        if i < 0 or i > self.n:  # Precondition
            return Exception()
        return self.add_before(self.get_node(i), x)

    def _remove(self, w: Node):
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1
        return w.x

    def remove(self, i: int):
        if i < 0 or i >= self.n:  raise IndexError()
        return self._remove(self.get_node(i))

    def size(self) -> int:
        return self.n

    def append(self, x: object):
        self.add(self.n, x)

    def isPalindrome(self) -> bool:
        if self.n <= 1:
            return True
        p = self.dummy.next  # Starts after the dummy node
        q = self.dummy.prev  # Starts before the dummy node
        while p != q and p.next != q:
            if p.x != q.x:
                return False
            p = p.next
            q = q.prev
        return True

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

    def reverse(self):
        current = self.dummy

        for i in range(self.n + 1):
            current.next, current.prev = current.prev, current.next
            current = current.prev