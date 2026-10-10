import unittest

from algoritmos.busca_binaria import busca_binaria


class TestBuscaBinaria(unittest.TestCase):
    def test_encontra(self):
        self.assertEqual(busca_binaria([1, 3, 5, 7, 9], 7), 3)

    def test_nao_encontra(self):
        self.assertEqual(busca_binaria([1, 3, 5], 4), -1)

    def test_lista_vazia(self):
        self.assertEqual(busca_binaria([], 1), -1)
