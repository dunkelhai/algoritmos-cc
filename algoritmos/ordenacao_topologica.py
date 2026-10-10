"""Ordenação topológica pelo algoritmo de Kahn."""

from collections import deque


def ordenacao_topologica(grafo):
    """Retorna uma ordem topológica ou levanta ValueError se houver ciclo."""
    grau = {v: 0 for v in grafo}
    for v in grafo:
        for w in grafo[v]:
            grau[w] = grau.get(w, 0) + 1
    fila = deque(sorted(v for v, g in grau.items() if g == 0))
    ordem = []
    while fila:
        v = fila.popleft()
        ordem.append(v)
        for w in grafo.get(v, []):
            grau[w] -= 1
            if grau[w] == 0:
                fila.append(w)
    if len(ordem) != len(grau):
        raise ValueError("o grafo possui ciclo")
    return ordem
