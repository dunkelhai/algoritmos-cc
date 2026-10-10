import unittest

from algoritmos.union_find import UnionFind


class TestUnionFind(unittest.TestCase):
    def test_uniao(self):
        uf = UnionFind(5)
        uf.une(0, 1)
        uf.une(3, 4)
        self.assertTrue(uf.conectados(0, 1))
        self.assertFalse(uf.conectados(1, 3))
        self.assertEqual(uf.componentes, 3)

    def test_uniao_repetida(self):
        uf = UnionFind(2)
        self.assertTrue(uf.une(0, 1))
        self.assertFalse(uf.une(1, 0))
