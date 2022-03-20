import cProfile
import random

from sorting import insertion_sort, quicksort, quicksort_lumoto

if __name__ == "__main__":
    numbers = [random.randint(0, 2**32) for _ in range(16000)]
    print("quicksort")
    cProfile.run("quicksort(numbers)")
    print("quicksort_lumoto")
    cProfile.run("quicksort_lumoto(numbers)")
    print("insertion_sort")
    cProfile.run("insertion_sort(numbers)")
