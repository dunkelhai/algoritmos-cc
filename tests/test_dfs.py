import unittest

from algoritmos.dfs import dfs, tem_ciclo


class TestDFS(unittest.TestCase):
    def test_ordem(self):
        grafo = {1: [2, 3], 2: [4], 3: [], 4: []}
        self.assertEqual(dfs(grafo, 1), [1, 2, 4, 3])

    def test_ciclo(self):
        self.assertTrue(tem_ciclo({1: [2], 2: [3], 3: [1]}))
        self.assertFalse(tem_ciclo({1: [2], 2: [3], 3: []}))
