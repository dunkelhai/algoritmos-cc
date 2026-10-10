import unittest

from algoritmos.mdc import euclides_estendido, inverso_modular, mdc, mmc


class TestMDC(unittest.TestCase):
    def test_mdc_mmc(self):
        self.assertEqual(mdc(48, 18), 6)
        self.assertEqual(mmc(4, 6), 12)

    def test_estendido(self):
        g, x, y = euclides_estendido(240, 46)
        self.assertEqual(g, 2)
        self.assertEqual(240 * x + 46 * y, 2)

    def test_inverso(self):
        self.assertEqual(inverso_modular(3, 11), 4)
        with self.assertRaises(ValueError):
            inverso_modular(2, 4)
