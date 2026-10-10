"""Distância de Levenshtein com memória O(min(m, n))."""


def distancia_edicao(a, b):
    if len(a) < len(b):
        a, b = b, a
    anterior = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        atual = [i]
        for j, cb in enumerate(b, 1):
            atual.append(min(
                anterior[j] + 1,
                atual[j - 1] + 1,
                anterior[j - 1] + (ca != cb),
            ))
        anterior = atual
    return anterior[-1]
