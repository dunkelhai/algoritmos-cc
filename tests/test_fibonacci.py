import unittest

from algoritmos.fibonacci import fibonacci, fibonacci_matriz


class TestFibonacci(unittest.TestCase):
    def test_valores(self):
        self.assertEqual([fibonacci(i) for i in range(10)], [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_matriz_igual_iterativo(self):
        for n in range(60):
            self.assertEqual(fibonacci_matriz(n), fibonacci(n))

    def test_negativo(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)
