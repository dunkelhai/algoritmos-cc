"""Árvore geradora mínima pelo algoritmo de Kruskal."""

from algoritmos.union_find import UnionFind


def kruskal(n, arestas):
    """`arestas`: [(peso, u, v)]. Retorna (custo_total, arestas_escolhidas)."""
    uf = UnionFind(n)
    escolhidas, custo = [], 0
    for peso, u, v in sorted(arestas):
        if uf.une(u, v):
            escolhidas.append((u, v, peso))
            custo += peso
    return custo, escolhidas
