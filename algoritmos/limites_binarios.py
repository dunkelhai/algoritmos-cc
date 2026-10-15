"""Limites de inserção em sequências ordenadas. O(log n)."""


def limite_inferior(lista, alvo):
    """Primeiro índice com valor >= alvo, ou len(lista) se não existir."""
    inicio, fim = 0, len(lista)
    while inicio < fim:
        meio = (inicio + fim) // 2
        if lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio
    return inicio


def limite_superior(lista, alvo):
    """Primeiro índice com valor > alvo, ou len(lista) se não existir."""
    inicio, fim = 0, len(lista)
    while inicio < fim:
        meio = (inicio + fim) // 2
        if alvo < lista[meio]:
            fim = meio
        else:
            inicio = meio + 1
    return inicio


def contar_ocorrencias(lista, alvo):
    """Conta ocorrências de alvo em uma sequência ordenada em O(log n)."""
    return limite_superior(lista, alvo) - limite_inferior(lista, alvo)
