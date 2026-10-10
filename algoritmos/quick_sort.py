"""Quick sort com partição de Lomuto. O(n log n) médio."""


def quick_sort(lista):
    itens = list(lista)
    _quick(itens, 0, len(itens) - 1)
    return itens


def _quick(itens, baixo, alto):
    if baixo < alto:
        p = _particiona(itens, baixo, alto)
        _quick(itens, baixo, p - 1)
        _quick(itens, p + 1, alto)


def _particiona(itens, baixo, alto):
    pivo = itens[alto]
    i = baixo
    for j in range(baixo, alto):
        if itens[j] <= pivo:
            itens[i], itens[j] = itens[j], itens[i]
            i += 1
    itens[i], itens[alto] = itens[alto], itens[i]
    return i
