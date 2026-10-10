"""Menores distâncias com Dijkstra (pesos não negativos)."""

import heapq


def dijkstra(grafo, origem):
    """`grafo`: {v: [(w, peso), ...]}. Retorna {v: distância}."""
    dist = {origem: 0}
    heap = [(0, origem)]
    while heap:
        d, v = heapq.heappop(heap)
        if d > dist.get(v, float("inf")):
            continue
        for w, peso in grafo.get(v, []):
            nd = d + peso
            if nd < dist.get(w, float("inf")):
                dist[w] = nd
                heapq.heappush(heap, (nd, w))
    return dist
