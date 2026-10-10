import unittest

from algoritmos.selection_sort import selection_sort


class TestSelectionSort(unittest.TestCase):
    def test_ordena(self):
        self.assertEqual(selection_sort([64, 25, 12, 22, 11]), [11, 12, 22, 25, 64])

    def test_um_elemento(self):
        self.assertEqual(selection_sort([7]), [7])
