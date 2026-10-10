import random
import unittest

from algoritmos.heap_sort import heap_sort


class TestHeapSort(unittest.TestCase):
    def test_ordena(self):
        self.assertEqual(heap_sort([12, 11, 13, 5, 6, 7]), [5, 6, 7, 11, 12, 13])

    def test_aleatorio(self):
        dados = [random.random() for _ in range(100)]
        self.assertEqual(heap_sort(dados), sorted(dados))
