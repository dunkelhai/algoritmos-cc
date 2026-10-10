import random
import unittest

from algoritmos.quick_sort import quick_sort


class TestQuickSort(unittest.TestCase):
    def test_ordena(self):
        self.assertEqual(quick_sort([10, 7, 8, 9, 1, 5]), [1, 5, 7, 8, 9, 10])

    def test_repetidos(self):
        self.assertEqual(quick_sort([2, 2, 1, 1]), [1, 1, 2, 2])

    def test_aleatorio(self):
        dados = [random.randint(0, 50) for _ in range(150)]
        self.assertEqual(quick_sort(dados), sorted(dados))
