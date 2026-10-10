import unittest

from algoritmos.ordenacao_topologica import ordenacao_topologica


class TestOrdenacaoTopologica(unittest.TestCase):
    def test_disciplinas(self):
        grafo = {
            "Algoritmos I": ["Estruturas de Dados"],
            "Estruturas de Dados": ["Grafos", "Compiladores"],
            "Grafos": [],
            "Compiladores": [],
        }
        ordem = ordenacao_topologica(grafo)
        self.assertLess(ordem.index("Algoritmos I"), ordem.index("Estruturas de Dados"))
        self.assertLess(ordem.index("Estruturas de Dados"), ordem.index("Grafos"))

    def test_ciclo(self):
        with self.assertRaises(ValueError):
            ordenacao_topologica({"a": ["b"], "b": ["a"]})
