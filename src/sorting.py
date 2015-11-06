from copy import copy
from math import floor
from random import random
from sorters import *
from time import time

SORTERS = [
    # Bubblesort(),
    # Insertionsort(),
    # Selectionsort(),
    Mergesort(),
    AltMergesort(),
    Quicksort()
]


def main():
    RUNS = 100
    lists = [[floor(random() * 1000) for i in range(10000)] for j in range(RUNS)]

    for sorter in SORTERS:
        work = copy(lists)
        t1 = time()
        for run in range(0, RUNS):
            _ = sorter.sorted(work[run])
        t2 = time()
        print("{}: took {}s, that is {}s per run!".format(sorter.__class__, t2-t1, (t2-t1)/RUNS))

if __name__ == "__main__":
    main()
