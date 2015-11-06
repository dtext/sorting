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


class Mergesort(Sorter):

    def sorted(self, l: list):
        # this implementation is not in-place
        return self.sort(list(l))

    def sort(self, l: list):
        if len(l) < 2:
            return l
        mid = len(l) // 2
        return self.merge(self.sort(l[:mid]), self.sort(l[mid:]))

    def merge(self, left: list, right: list) -> list:
        result = []
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        # add items from list that has elements left
        rest = right if len(left) == 0 else left
        for el in rest:
            result.append(el)
        return result


class Quicksort(Sorter):

    def sorted(self, l: list):
        # this implementation is not in-place
        return self.sort(l)

    def sort(self, l: list):
        if len(l) < 2:
            return l
        pivot = l[len(l)//2]
        left, right, pivots = [], [], []
        for x in l:
            if x < pivot:
                left.append(x)
            elif x == pivot:
                pivots.append(x)
            else:
                right.append(x)
        return self.sort(left) + pivots + self.sort(right)

