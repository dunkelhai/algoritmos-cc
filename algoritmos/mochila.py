"""Mochila 0/1 por programação dinâmica. O(n · capacidade)."""


def mochila(pesos, valores, capacidade):
    melhor = [0] * (capacidade + 1)
    for peso, valor in zip(pesos, valores):
        for c in range(capacidade, peso - 1, -1):
            melhor[c] = max(melhor[c], melhor[c - peso] + valor)
    return melhor[capacidade]
