"""Implementations of some sorting"""
import random
from Interfaces import List


def linear_search(a: List, x):
    for i in range(len(a)):     # for every element in the array a
        if a[i] == x:           # if the element at index i in the array a equals the value we're searching for (x)
            return i            # return that element
    return None                 # else, return None


def binary_search(a: List, x):
    l = 0               # left bound
    r = len(a) - 1      # right bound
    while l <= r:
        m = (l + r) // 2
        if x == a[m]:   # if the value we're searching for (x) equals the element at index m in the array a
            return m        # we return m
        elif x < a[m]:  # else, if the value we are searching for (x) is less than the element at index m in the array a
            a[0:m]          # that means x is in the first half of the array
            r = m - 1       # we'll look at all the values to the left of it
        else:
            a[m:r]          # else, x is in the second half of the array
            l = m + 1       # we'll look at all the values to the right of it
    return None


def _merge(a0: List, a1: List, a: List):
    i0 = 0      # tracking position of the first subarray
    i1 = 0      # tracking position of the second subarray
    n = len(a)  # number of elements in the array

    for i in range(n):      # for every element in the array
        if i0 >= len(a0):       # if the tracking position in the 1st subarray (i0) >= the len of the 1st subarray
            a[i] = a1[i1]           # the element at index i in the array a = the element i1 in the 2nd subarray
            i1 += 1                 # increment the tracking position of the 2nd subarray
        elif i1 >= len(a1):     # else, if tracking position of 2nd subarray >= len of 2nd subarray
            a[i] = a0[i0]           # the element at index i in the array = the element i0 in the 1st subarray
            i0 += 1                 # increment the tracking position of the 1st subarray
        elif a0[i0] <= a1[i1]:  
            a[i] = a0[i0]
            i0 += 1
        else:
            a[i] = a1[i1]
            i1 += 1


def merge_sort(a: List):
    n = len(a)

    if n == 0 or n == 1:
        return a

    m = n // 2      # mid
    a0 = a[0:m]     # first half of the array
    a1 = a[m:n]     # second half of the array

    # Recursively sort a0 and a1
    merge_sort(a0)
    merge_sort(a1)

    # Merge a0 and a1
    _merge(a0, a1, a)


def _partition_f(a: List, start, end):
    pivot = a[start]
    l = start + 1
    r = end

    while l <= r:
        # Find element larger than pivot from left
        while l <= r and a[l] <= pivot:     # traversing from start-to-end
            l += 1

        # Find element smaller than pivot from right
        while r >= l and a[r] > pivot:      # traversing from end-to-start
            r -= 1

        # Swap elements if pointers haven't crossed
        if l < r:
            a[l], a[r] = a[r], a[l]

    # Place pivot in its correct position
    a[start], a[r] = a[r], a[start]
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


def _partition_r(a: List, start, end):
    # Choose random element, then swap that random element with the first element to be the pivot
    pivot_r = random.randint(start, end)
    a[start], a[pivot_r] = a[pivot_r], a[start]

    pivot = a[start]
    l = start + 1
    r = end

    while l <= r:
        # Find element larger than pivot from left
        while l <= r and a[l] <= pivot:     # traversing from start-to-end
            l += 1

        # Find element smaller than pivot from right
        while r >= l and a[r] > pivot:      # traversing from end-to-start
            r -= 1

        # Swap elements if pointers haven't crossed
        if l < r:
            a[l], a[r] = a[r], a[l]

    # Place pivot in its correct position
    a[start], a[r] = a[r], a[start]
    return r


def _quick_sort_r(a: List, start, end):
    """
    Helper function that uses a random element as pivot to sort the ArrayList object a
    """
    if start < end:
        p = _partition_r(a, start, end)

        # Recursion
        _quick_sort_r(a, start, p - 1)  # first half
        _quick_sort_r(a, p + 1, end)    # second half


def quick_sort(a: List, p=True):
    """
    sorts an ArrayList a using the quick sort algorithm.
    If parameter p is True, the quick sort algorithm uses a randomly chosen element from a as pivot.
    Otherwise, the quick sort algorithm uses the first element as pivot.
    """
    if p:
        _quick_sort_r(a, 0, len(a) - 1)
    else:
        _quick_sort_f(a, 0, len(a) - 1)
