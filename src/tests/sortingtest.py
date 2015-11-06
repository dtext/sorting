import unittest
from random import random

class SorterTest(unittest.TestCase):

    def setUp(self):
        self.sorters = [

        ]

    def test_empty(self):
        for sorter in self.sorters:
            self.assertEqual(len(sorter.sorted([])), 0)

    def test_one(self):
        for sorter in self.sorters:
            self.assertEqual(len(sorter.sorted["one"]), 1)

    def test_number(self):
        l = [random() for i in range(100)]
        for sorter in self.sorters:
            self.assertEqual(sorter.sorted(l), sorted(l))

    def test_string(self):
        s = "ailwefawlILWESFBNSLIEFWIWFleifwnslifenFLIWENLISNqrwpoueitrwezuiopgsdfjhklöaljkfyvmcx"
        for sorter in self.sorters:
            self.assertEqual(sorter.sorted(s), sorted(s))


if __name__ == '__main__':
    unittest.main()
