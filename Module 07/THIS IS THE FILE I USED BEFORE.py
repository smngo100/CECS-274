"""Implementations of some sorting"""
import random

from Interfaces import List


def linear_search(a: List, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return None


def binary_search(a: List, x):
    l = 0               # left bound
    r = len(a) - 1      # right bound
    while l <= r:
        m = (l + r) // 2
        if x == a[m]:
            return m
        elif x < a[m]:
            a[0:m]
            r = m - 1
        else:
            a[m:r]
            l = m + 1
    return None


def _merge(a0: List, a1: List, a: List):
    i0 = 0
    i1 = 0
    n = len(a)

    for i in range(n - 1):
        if i0 >= len(a0):
            a[i] = a1[i1]
            i1 += 1
        elif i1 >= len(a1):
            a[i] = a0[i0]
            i0 += 1
        elif a0[i0] <= a1[i1]:
            a[i] = a0[i0]
            i0 += 1
        else:
            a[i] = a1[i1]
            i1 += 1


def merge_sort(a: List):
    #a.a.sort()
    n = len(a)

    if len(a) <= 1:
        return a

    m = n // 2       # mid
    a0 = a[:m]       # first half of the array
    a1 = a[m:]       # second half of the array

    # Recursively sort a0 and a1
    a0 = merge_sort(a0)
    a1 = merge_sort(a1)

    # Merge a0 and a1
    return _merge(a0, a1, a)


def _partition_f(a: List, start, end):
    n = len(a)
    pivot = a[start]
    l = start
    r = end - 1

    while l < r:
        while l <= r and a[l] <= pivot:     # traversing from start-to-end
            l += 1
        while r >= l and a[r] > pivot:      # traversing from end-to-start
            r -= 1

        if l < r:
            a[l], a[r] = a[r], a[l]

    if a[r] > pivot:
        a[r], a[start] = a[start], a[r]

    return r


def _quick_sort_f(a: List, start, end):
    """
    Helper function that uses the first element as pivot to sort the ArrayList object a
    """
    if start < end:
        p = _partition_f(a, start, end)

        # Recursion
        _quick_sort_f(a, start, p - 1)  # first half
        _quick_sort_f(a, p + 1, end)    # second half
    elif start >= end:
        return a


def _partition_r(a: List, start, end):
    n = len(a)
    pivot_r = random.randint(start)
    l = start
    r = end - 1

    a[start], a[pivot_r] = a[pivot_r], a[start]
    return _partition_f


def _quick_sort_r(a: List, start, end):
    """
    Helper function that uses a random element as pivot to sort the ArrayList object a
    """
    if start < end:
        p = _partition_r(a, start, end)

        # Recursion
        _quick_sort_r(a, start, p - 1)  # first half
        _quick_sort_r(a, p + 1, end)    # second half
    elif start >= end:
        return a


def quick_sort(a: List, p=True):
    """
    sorts an ArrayList a using the quick sort algorithm.
    If parameter p is True, the quick sort algorithm uses a randomly chosen element from a as pivot.
    Otherwise, the quick sort algorithm uses the first element as pivot.
    """
    if p:
        #a.a.sort()
        _quick_sort_r(a, 0, len(a) - 1)
    else:
        #a.a.sort()
        _quick_sort_f(a, 0, len(a) - 1)
