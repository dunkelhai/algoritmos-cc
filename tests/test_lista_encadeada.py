import unittest

from algoritmos.lista_encadeada import ListaEncadeada


class TestListaEncadeada(unittest.TestCase):
    def test_construcao(self):
        self.assertEqual(list(ListaEncadeada([1, 2, 3])), [1, 2, 3])

    def test_remove(self):
        lista = ListaEncadeada([1, 2, 3])
        self.assertTrue(lista.remove(2))
        self.assertFalse(lista.remove(9))
        self.assertEqual(list(lista), [1, 3])
        self.assertEqual(len(lista), 2)

    def test_inverte(self):
        lista = ListaEncadeada([1, 2, 3])
        lista.inverte()
        self.assertEqual(list(lista), [3, 2, 1])
