import unittest

from algoritmos.bfs import bfs, menor_caminho

GRAFO = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D", "E"],
    "D": ["F"],
    "E": ["F"],
    "F": [],
}


class TestBFS(unittest.TestCase):
    def test_ordem(self):
        self.assertEqual(bfs(GRAFO, "A"), ["A", "B", "C", "D", "E", "F"])

    def test_menor_caminho(self):
        self.assertEqual(menor_caminho(GRAFO, "A", "F"), ["A", "B", "D", "F"])

    def test_sem_caminho(self):
        self.assertIsNone(menor_caminho(GRAFO, "F", "A"))
