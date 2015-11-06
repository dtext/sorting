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

