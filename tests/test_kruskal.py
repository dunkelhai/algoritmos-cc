import unittest

from algoritmos.kruskal import kruskal


class TestKruskal(unittest.TestCase):
    def test_custo(self):
        arestas = [(10, 0, 1), (6, 0, 2), (5, 0, 3), (15, 1, 3), (4, 2, 3)]
        custo, escolhidas = kruskal(4, arestas)
        self.assertEqual(custo, 19)
        self.assertEqual(len(escolhidas), 3)
