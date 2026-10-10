import unittest

from algoritmos.crivo_eratostenes import primos_ate


class TestCrivo(unittest.TestCase):
    def test_ate_30(self):
        self.assertEqual(primos_ate(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    def test_pequenos(self):
        self.assertEqual(primos_ate(1), [])
        self.assertEqual(primos_ate(2), [2])

    def test_quantidade(self):
        self.assertEqual(len(primos_ate(1000)), 168)
