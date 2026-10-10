"""Heap sort usando max-heap in-place. O(n log n)."""


def heap_sort(lista):
    itens = list(lista)
    n = len(itens)
    for i in range(n // 2 - 1, -1, -1):
        _desce(itens, n, i)
    for fim in range(n - 1, 0, -1):
        itens[0], itens[fim] = itens[fim], itens[0]
        _desce(itens, fim, 0)
    return itens


def _desce(itens, n, i):
    while True:
        maior = i
        esq, dir_ = 2 * i + 1, 2 * i + 2
        if esq < n and itens[esq] > itens[maior]:
            maior = esq
        if dir_ < n and itens[dir_] > itens[maior]:
            maior = dir_
        if maior == i:
            return
        itens[i], itens[maior] = itens[maior], itens[i]
        i = maior
