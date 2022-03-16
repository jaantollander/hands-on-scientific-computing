#!/usr/bin/env python3
import random
import copy

def insertion_sort(arr):
    a = copy.copy(arr)

    for i in range(len(a)):
        j = i - 1
        k = a[i]
        while j >= 0 and k < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = k

    return a

# A quicksort implementation that does not use Lumoto partition
def quicksort(arr):
    a = copy.copy(arr)

    if len(a) <= 1:
        return a
    pivot = a[0]
    left  = [num for num in a[1:] if num <= pivot]
    right = [num for num in a[1:] if num > pivot]
    return quicksort(left) + [pivot] + quicksort(right)

# Lumoto partition
def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo
    j = lo
    while(j < hi):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1
    arr[i], arr[hi] = arr[hi], arr[i]
    return i

# A quicksort implementation that uses Lumoto partition
def _quicksort(arr, lo, hi):
    if len(arr) <= 1:
        return arr

    if lo >= hi:
        return arr

    p = partition(arr, lo, hi)

    _quicksort(arr, lo, p - 1)
    _quicksort(arr, p + 1, hi)
    return arr

# A wrapper function for _quicksort
def quicksort_lumoto(arr):
    a = copy.copy(arr)
    return _quicksort(a, 0, len(a) - 1)

if __name__ == "__main__":
    # Sort a list of size 16000
    numbers = [random.randint(0, 2**32) for _ in range(16000)]
    for sort in [quicksort_lumoto, quicksort, insertion_sort]:
        print("Now sorting using {}".format(sort.__name__))
        sort(numbers)