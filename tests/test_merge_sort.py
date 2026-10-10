import random
import unittest

from algoritmos.merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):
    def test_ordena(self):
        self.assertEqual(merge_sort([38, 27, 43, 3, 9, 82, 10]), [3, 9, 10, 27, 38, 43, 82])

    def test_aleatorio(self):
        dados = [random.randint(-100, 100) for _ in range(200)]
        self.assertEqual(merge_sort(dados), sorted(dados))
