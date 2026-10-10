import unittest

from algoritmos.bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    def test_ordena(self):
        self.assertEqual(bubble_sort([5, 2, 9, 1, 5]), [1, 2, 5, 5, 9])

    def test_nao_altera_original(self):
        original = [3, 1, 2]
        bubble_sort(original)
        self.assertEqual(original, [3, 1, 2])

    def test_vazia(self):
        self.assertEqual(bubble_sort([]), [])
