"""Counting sort para inteiros. O(n + k)."""


def counting_sort(lista):
    if not lista:
        return []
    menor, maior = min(lista), max(lista)
    contagem = [0] * (maior - menor + 1)
    for x in lista:
        contagem[x - menor] += 1
    resultado = []
    for deslocamento, qtd in enumerate(contagem):
        resultado.extend([deslocamento + menor] * qtd)
    return resultado
