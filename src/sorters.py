from abc import ABCMeta, abstractmethod


class Sorter(metaclass=ABCMeta):

    @abstractmethod
    def sorted(self, l: list) -> list:
        pass


class Bubblesort(Sorter):

    def sorted(self, l: list) -> list:
        r = list(l)
        swapped = True
        while(swapped):
            swapped = False
            for i in range(len(r) - 1):
                if r[i] > r[i+1]:
                    swapped = True
                    r[i], r[i+1] = r[i+1], r[i]
        return r

class Insertionsort(Sorter):

    def sorted(self, l: list) -> list:
        r = list(l)
        for i in range(len(r)):
            j = i
            cmp = r[i]
            while j and r[j-1] > cmp:
                r[j] = r[j-1]
                j -= 1
            r[j] = cmp
        return r
