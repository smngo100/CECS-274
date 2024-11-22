import numpy as np
import math
from Interfaces import Queue
from Interfaces import Tree


def left(i: int) -> int:    # i = index of the current node
    """
    helper method; returns the index of the left child of the element at index i
    """
    return 2 * i + 1    # index of the left child


def right(i: int) -> int:
    """
    helper method; returns the index of the right child of the element at index i
    """
    return 2 * (i + 1)  # index of the right child


def parent(i: int) -> int:
    """
    helper method; returns the index of the parent of the element at index i
    """
    return (i - 1) // 2 # index of the parent


def _new_array(n: int) -> np.array:
    """
    helper method; creates a new numpy array of 0's of size n
    """
    return np.zeros(n, object)


class BinaryHeap(Queue, Tree):
    def __init__(self):
        self.a = _new_array(1)
        self.n = 0

    def add(self, x: object):
        if self.n == len(self.a):
            self._resize()
        self.a[self.n] = x
        self.n += 1
        self._bubble_up_last()
        return True

    def remove(self):
        if self.n == 0:
            raise IndexError
        x = self.a[0]
        self.a[0] = self.a[self.n -1]
        self.n -= 1
        self._trickle_down_root()
        if 3 * self.n < len(self.a):
            self._resize()
        return x

    def depth(self, u) -> int:
        for i in range(self.n):
            if self.a[i] == u:
                return int(math.log2(i + 1))
        raise ValueError(f"{u} is not found in the binary tree.")

    def height(self) -> int:
        if self.n == 0:
            return 0
        return int(math.log2(self.n))

    def bf_order(self) -> list:
        return list(self.a[0:self.n])

    def in_order(self) -> list:
        indices = self._in_order(0)
        return [self.a[i] for i in indices]

    # in order: left subtree --> current node --> right subtree
    def _in_order(self, i):
        indices = []
        l_idx = left(i)
        r_idx = right(i)

        # Visit left subtree
        if 0 <= l_idx < self.n:
            indices.extend(self._in_order(l_idx))

        # Visit current node
        if 0 <= i < self.n:
            indices.append(i)

        # Visit right subtree
        if 0 <= r_idx < self.n:
            indices.extend(self._in_order(r_idx))

        return indices

    def post_order(self) -> list:
        indices = self._post_order(0)
        return [self.a[i] for i in indices]

    # post order: left subtree --> right subtree --> current node
    def _post_order(self, i):
        indices = []
        l_idx = left(i)
        r_idx = right(i)

        # Visit left subtree
        if 0 <= l_idx < self.n:
            indices.extend(self._post_order(l_idx))

        # Visit right subtree
        if 0 <= r_idx < self.n:
            indices.extend(self._post_order(r_idx))

        # Visit current node
        if 0 <= i < self.n:
            indices.append(i)

        return indices

    def pre_order(self) -> list:
        indices = self._pre_order(0)
        return [self.a[i] for i in indices]

    # pre-order: current node --> left subtree --> right subtree
    def _pre_order(self, i):
        indices = []
        l_idx = left(i)
        r_idx = right(i)

        # Visit current node
        if 0 <= i < self.n:
            indices.append(i)

        # Visit left subtree
        if 0 <= l_idx < self.n:
            indices.extend(self._pre_order(l_idx))

        # Visit right subtree
        if 0 <= r_idx < self.n:
            indices.extend(self._pre_order(r_idx))

        return indices

    def size(self) -> int:
        return self.n

    def find_min(self):
        if self.n == 0: raise IndexError()
        return self.a[0]

    def _bubble_up_last(self):
        i = self.n - 1  # initialize i as index of last element
        p_idx = parent(i)   # initialize p_idx as parent of i

        # while i > 0 and element at i is smaller than its parent
        while i > 0 and self.a[i] < self.a[p_idx]:
            self.a[i], self.a[p_idx] = self.a[p_idx], self.a[i]  # swap elements
            i = p_idx           # update i to be p_idx
            p_idx = parent(i)   # update p_idx to be parent of new i

    def _resize(self):
        b = _new_array(max(1, 2 * len(self.a)))
        for i in range(self.n):
            b[i] = self.a[i]
        self.a = b

    def _trickle_down_root(self):
        i = 0   # initialize i as root index

        # Get indices of left and right children
        l_idx = left(i)
        r_idx = right(i)

        # while i and its children are valid indices and a[i] is larger than its children
        while (i < self.n and l_idx < self.n and r_idx < self.n) and (self.a[i] > self.a[l_idx] or self.a[i] > self.a[r_idx]):
            min_idx = i

            # compare with left child
            if l_idx < self.n and self.a[l_idx] < self.a[min_idx]:
                min_idx = l_idx

            # compare with right child
            if r_idx < self.n and self.a[r_idx] < self.a[min_idx]:
                min_idx = r_idx

            self.a[i], self.a[min_idx] = self.a[min_idx], self.a[i] # swap elements
            i = min_idx # update i to min_idx

            # update children indices for new i
            l_idx = left(i)
            r_idx = right(i)

    def __str__(self):
        return str(self.a[0:self.n])