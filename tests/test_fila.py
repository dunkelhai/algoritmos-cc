import unittest

from algoritmos.fila import Fila


class TestFila(unittest.TestCase):
    def test_fifo(self):
        f = Fila()
        for i in range(3):
            f.enfileira(i)
        self.assertEqual(f.desenfileira(), 0)
        f.enfileira(3)
        self.assertEqual([f.desenfileira() for _ in range(3)], [1, 2, 3])

    def test_vazia_erro(self):
        with self.assertRaises(IndexError):
            Fila().frente()
