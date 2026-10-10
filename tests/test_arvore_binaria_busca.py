import unittest

from algoritmos.arvore_binaria_busca import ArvoreBinariaBusca


class TestArvoreBinariaBusca(unittest.TestCase):
    def setUp(self):
        self.arvore = ArvoreBinariaBusca()
        for x in [50, 30, 70, 20, 40, 60, 80]:
            self.arvore.insere(x)

    def test_em_ordem(self):
        self.assertEqual(self.arvore.em_ordem(), [20, 30, 40, 50, 60, 70, 80])

    def test_contem(self):
        self.assertTrue(self.arvore.contem(60))
        self.assertFalse(self.arvore.contem(65))

    def test_altura(self):
        self.assertEqual(self.arvore.altura(), 3)
