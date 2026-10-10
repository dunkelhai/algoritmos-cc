import unittest

from algoritmos.counting_sort import counting_sort


class TestCountingSort(unittest.TestCase):
    def test_ordena(self):
        self.assertEqual(counting_sort([4, 2, 2, 8, 3, 3, 1]), [1, 2, 2, 3, 3, 4, 8])

    def test_negativos(self):
        self.assertEqual(counting_sort([-3, 0, -1, 2]), [-3, -1, 0, 2])

    def test_vazia(self):
        self.assertEqual(counting_sort([]), [])
