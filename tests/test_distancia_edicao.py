import unittest

from algoritmos.distancia_edicao import distancia_edicao


class TestDistanciaEdicao(unittest.TestCase):
    def test_classico(self):
        self.assertEqual(distancia_edicao("kitten", "sitting"), 3)

    def test_iguais(self):
        self.assertEqual(distancia_edicao("ciencia", "ciencia"), 0)

    def test_vazia(self):
        self.assertEqual(distancia_edicao("", "abc"), 3)
