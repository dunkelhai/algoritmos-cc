import unittest

from algoritmos.insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):
    def test_ordena(self):
        self.assertEqual(insertion_sort([4, 3, 2, 10, 12, 1]), [1, 2, 3, 4, 10, 12])

    def test_negativos(self):
        self.assertEqual(insertion_sort([0, -1, -5, 3]), [-5, -1, 0, 3])
