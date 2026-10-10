"""Selection sort. O(n²), faz no máximo n trocas."""


def selection_sort(lista):
    itens = list(lista)
    for i in range(len(itens)):
        menor = i
        for j in range(i + 1, len(itens)):
            if itens[j] < itens[menor]:
                menor = j
        itens[i], itens[menor] = itens[menor], itens[i]
    return itens
