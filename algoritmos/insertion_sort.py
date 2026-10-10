"""Insertion sort. O(n²), estável, bom para listas quase ordenadas."""


def insertion_sort(lista):
    itens = list(lista)
    for i in range(1, len(itens)):
        chave = itens[i]
        j = i - 1
        while j >= 0 and itens[j] > chave:
            itens[j + 1] = itens[j]
            j -= 1
        itens[j + 1] = chave
    return itens
