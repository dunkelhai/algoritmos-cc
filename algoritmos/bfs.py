"""Busca em largura em grafo representado por lista de adjacência."""

from collections import deque


def bfs(grafo, origem):
    """Retorna a ordem de visita a partir de `origem`."""
    visitados = {origem}
    ordem = []
    fila = deque([origem])
    while fila:
        v = fila.popleft()
        ordem.append(v)
        for w in grafo.get(v, []):
            if w not in visitados:
                visitados.add(w)
                fila.append(w)
    return ordem


def menor_caminho(grafo, origem, destino):
    """Menor caminho (em número de arestas) ou None."""
    anterior = {origem: None}
    fila = deque([origem])
    while fila:
        v = fila.popleft()
        if v == destino:
            caminho = []
            while v is not None:
                caminho.append(v)
                v = anterior[v]
            return caminho[::-1]
        for w in grafo.get(v, []):
            if w not in anterior:
                anterior[w] = v
                fila.append(w)
    return None
