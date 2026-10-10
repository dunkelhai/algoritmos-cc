import unittest

from algoritmos.mochila import mochila


class TestMochila(unittest.TestCase):
    def test_classico(self):
        self.assertEqual(mochila([10, 20, 30], [60, 100, 120], 50), 220)

    def test_nada_cabe(self):
        self.assertEqual(mochila([5], [10], 4), 0)
