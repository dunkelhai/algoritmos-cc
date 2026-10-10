"""Bubble sort com parada antecipada. O(n²)."""


def bubble_sort(lista):
    itens = list(lista)
    n = len(itens)
    for i in range(n):
        trocou = False
        for j in range(n - i - 1):
            if itens[j] > itens[j + 1]:
                itens[j], itens[j + 1] = itens[j + 1], itens[j]
                trocou = True
        if not trocou:
            break
    return itens
