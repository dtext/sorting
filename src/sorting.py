from copy import copy
from math import floor
from random import random
from sorters import *
from time import time

SORTERS = [
    Timsort(),
    # Bubblesort(),
    # Insertionsort(),
    # Selectionsort(),
    Mergesort(),
    AltMergesort(),
    Quicksort()
]


def main():
    n_runs = 100
    n_elements = 10000
    random_data = [[floor(random() * n_elements) for i in range(n_elements)] for j in range(n_runs)]
    sorted_data = [range(n_elements) for i in range(n_runs)]
    inverted_data = [range(n_elements) for i in range(n_runs)]

    categories = {
        "\nRandom data:": random_data,
        "\nAlready sorted data:": sorted_data,
        "\nInverted data:": inverted_data
    }
    print("\nStarting sorting algorithm benchmark using these settings:")
    print("Random data, already sorted data, inverted data")
    print("{} runs and {} elements each".format(n_runs, n_elements))
    for caption, data in categories.items():
        print(caption)
        for sorter in SORTERS:
            work = copy(data)
            t1 = time()
            for run in range(0, n_runs):
                _ = sorter.sorted(work[run])
            t2 = time()
            print("{}: took {}s, that is {}s per run!".format(str(sorter.__class__)[16:-2], t2-t1, (t2-t1)/n_runs))

if __name__ == "__main__":
    main()
