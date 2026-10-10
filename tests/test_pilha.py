import unittest

from algoritmos.pilha import Pilha, parenteses_balanceados


class TestPilha(unittest.TestCase):
    def test_lifo(self):
        p = Pilha()
        p.empilha(1)
        p.empilha(2)
        self.assertEqual(p.topo(), 2)
        self.assertEqual(p.desempilha(), 2)
        self.assertEqual(len(p), 1)

    def test_vazia_erro(self):
        with self.assertRaises(IndexError):
            Pilha().desempilha()

    def test_parenteses(self):
        self.assertTrue(parenteses_balanceados("{[()()]}"))
        self.assertFalse(parenteses_balanceados("([)]"))
        self.assertFalse(parenteses_balanceados("(("))
