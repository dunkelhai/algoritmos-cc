import unittest

from algoritmos.dijkstra import dijkstra


class TestDijkstra(unittest.TestCase):
    def test_distancias(self):
        grafo = {
            "A": [("B", 4), ("C", 1)],
            "C": [("B", 2), ("D", 5)],
            "B": [("D", 1)],
        }
        self.assertEqual(dijkstra(grafo, "A"), {"A": 0, "C": 1, "B": 3, "D": 4})

    def test_inalcancavel(self):
        self.assertNotIn("Z", dijkstra({"A": []}, "A"))
