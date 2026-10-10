import unittest

from algoritmos.lcs import lcs


class TestLCS(unittest.TestCase):
    def test_classico(self):
        self.assertEqual(len(lcs("ABCBDAB", "BDCABA")), 4)

    def test_exemplo(self):
        self.assertEqual(lcs("AGGTAB", "GXTXAYB"), "GTAB")

    def test_vazio(self):
        self.assertEqual(lcs("", "abc"), "")
