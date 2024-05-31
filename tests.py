import unittest
from random import shuffle
from bars import State, Bar
from sorter import Sorter

class TestSorter(unittest.TestCase):
    def setUp(self):
        self.sorter = Sorter()
        self.bars = [Bar(i) for i in range(1, 100, 100 // 10)]
        self.expected_bars = [Bar(i, State.SORTED) for i in range(1, 100, 100 // 10)]

    def __get_bars(self):
        bars = self.bars.copy()
        shuffle(bars)
        return bars
    
    def test_binary_sort(self):
        bars = self.__get_bars()
        self.sorter.bubble_sort(bars)
        self.assertEqual(bars, self.expected_bars)

    def test_selection_sort(self):
        bars = self.__get_bars()
        self.sorter.selection_sort(bars)
        self.assertEqual(bars, self.expected_bars)

    def test_quick_sort(self):
        bars = self.__get_bars()
        self.sorter.quick_sort(bars)
        self.assertEqual(bars, self.expected_bars)   

    def test_merge_sort(self):
        bars = self.__get_bars()
        self.sorter.merge_sort(bars)
        self.assertEqual(bars, self.expected_bars)   

    def test_insertion_sort(self):
        bars = self.__get_bars()
        self.sorter.insertion_sort(bars)
        self.assertEqual(bars, self.expected_bars)   

if __name__ == "__main__":
    unittest.main()
