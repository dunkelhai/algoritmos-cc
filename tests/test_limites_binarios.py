import bisect
import itertools
import unittest

from algoritmos.limites_binarios import (
    contar_ocorrencias,
    limite_inferior,
    limite_superior,
)


class TestLimitesBinarios(unittest.TestCase):
    def test_duplicatas(self):
        lista = [1, 2, 2, 2, 4]
        self.assertEqual(limite_inferior(lista, 2), 1)
        self.assertEqual(limite_superior(lista, 2), 4)
        self.assertEqual(contar_ocorrencias(lista, 2), 3)

    def test_vazia(self):
        self.assertEqual(limite_inferior([], 1), 0)
        self.assertEqual(limite_superior([], 1), 0)
        self.assertEqual(contar_ocorrencias([], 1), 0)

    def test_ausente_e_extremos(self):
        for alvo, esperado in [(-3, 0), (0, 1), (8, 3)]:
            with self.subTest(alvo=alvo):
                self.assertEqual(limite_inferior([-2, 1, 7], alvo), esperado)
                self.assertEqual(limite_superior([-2, 1, 7], alvo), esperado)
                self.assertEqual(contar_ocorrencias([-2, 1, 7], alvo), 0)

    def test_todos_iguais(self):
        self.assertEqual(limite_inferior([5] * 4, 5), 0)
        self.assertEqual(limite_superior([5] * 4, 5), 4)

    def test_sequencia_de_strings(self):
        self.assertEqual(limite_inferior(("a", "b", "b", "z"), "b"), 1)
        self.assertEqual(limite_superior(("a", "b", "b", "z"), "b"), 3)

    def test_compara_bisect_e_contagem(self):
        for tamanho in range(6):
            for valores in itertools.combinations_with_replacement(range(-2, 3), tamanho):
                lista = list(valores)
                for alvo in range(-3, 4):
                    with self.subTest(lista=lista, alvo=alvo):
                        self.assertEqual(limite_inferior(lista, alvo), bisect.bisect_left(lista, alvo))
                        self.assertEqual(limite_superior(lista, alvo), bisect.bisect_right(lista, alvo))
                        self.assertEqual(contar_ocorrencias(lista, alvo), lista.count(alvo))
                self.assertEqual(lista, list(valores))
