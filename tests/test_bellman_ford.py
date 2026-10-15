import copy
import random
import unittest

from algoritmos.bellman_ford import bellman_ford
from algoritmos.dijkstra import dijkstra


class TestBellmanFord(unittest.TestCase):
    def test_pesos_negativos(self):
        grafo = {"A": [("B", 4), ("C", 5)], "B": [("C", -2)], "C": [("D", 3)]}
        self.assertEqual(bellman_ford(grafo, "A"), {"A": 0, "B": 4, "C": 2, "D": 5})

    def test_relaxamento_em_varias_passagens(self):
        grafo = {"C": [("D", -1)], "B": [("C", -1)], "A": [("B", 4)]}
        self.assertEqual(bellman_ford(grafo, "A"), {"A": 0, "B": 4, "C": 3, "D": 2})

    def test_ciclo_negativo_alcancavel(self):
        grafo = {"A": [("B", 1)], "B": [("C", -2)], "C": [("B", 1)]}
        with self.assertRaisesRegex(ValueError, "ciclo negativo"):
            bellman_ford(grafo, "A")

    def test_ciclo_negativo_desconectado(self):
        grafo = {"A": [("B", 2)], "X": [("Y", -2)], "Y": [("X", 1)]}
        self.assertEqual(bellman_ford(grafo, "A"), {"A": 0, "B": 2})

    def test_laco_negativo_na_origem(self):
        with self.assertRaises(ValueError):
            bellman_ford({"A": [("A", -1)]}, "A")

    def test_ciclo_de_peso_zero(self):
        self.assertEqual(bellman_ford({0: [(1, -1)], 1: [(0, 1)]}, 0), {0: 0, 1: -1})

    def test_grafo_vazio_e_origem_ausente(self):
        self.assertEqual(bellman_ford({}, "A"), {"A": 0})
        self.assertEqual(bellman_ford({"B": []}, "A"), {"A": 0})

    def test_vertices_sem_ordenacao(self):
        grafo = {None: [("B", 1), (2, 1)], "B": [(2, -1)]}
        self.assertEqual(bellman_ford(grafo, None), {None: 0, "B": 1, 2: 0})

    def test_arestas_paralelas_e_nao_altera_grafo(self):
        grafo = {0: [(1, 8), (1, 2)], 1: [(1, 0)]}
        original = copy.deepcopy(grafo)
        self.assertEqual(bellman_ford(grafo, 0), {0: 0, 1: 2})
        self.assertEqual(grafo, original)

    def test_compara_dijkstra_com_pesos_nao_negativos(self):
        gerador = random.Random(42)
        for _ in range(30):
            grafo = {
                v: [(w, gerador.randrange(10)) for w in range(8) if gerador.random() < 0.25]
                for v in range(8)
            }
            for origem in grafo:
                with self.subTest(grafo=grafo, origem=origem):
                    self.assertEqual(bellman_ford(grafo, origem), dijkstra(grafo, origem))
