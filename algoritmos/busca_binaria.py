"""Busca binária em lista ordenada. O(log n)."""


def busca_binaria(lista, alvo):
    """Retorna o índice de `alvo` em `lista` (ordenada) ou -1."""
    inicio, fim = 0, len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio
        if lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1
