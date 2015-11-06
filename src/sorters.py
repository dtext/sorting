from abc import ABCMeta, abstractmethod


class Sorter(metaclass=ABCMeta):

    @abstractmethod
    def sort(self, l: list):
        pass

    def sorted(self, l: list) -> list:
        r = list(l)
        self.sort(r)
        return r


class Bubblesort(Sorter):

    def sort(self, l: list):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(l) - 1):
                if l[i] > l[i+1]:
                    swapped = True
                    l[i], l[i+1] = l[i+1], l[i]


class Insertionsort(Sorter):

    def sort(self, l: list):
        for i in range(len(l)):
            j = i
            cmp = l[i]
            while j and l[j-1] > cmp:
                l[j] = l[j-1]
                j -= 1
            l[j] = cmp


class Selectionsort(Sorter):

    def sort(self, l: list):
        for i in range(len(l)):
            pmin = i
            for j in range(i + 1, len(l)):
                if l[j] < l[pmin]:
                    pmin = j
            l[i], l[pmin] = l[pmin], l[i]
