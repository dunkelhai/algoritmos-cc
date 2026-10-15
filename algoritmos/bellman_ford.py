"""Menores distâncias em grafos dirigidos com pesos negativos. O(V * E)."""


def bellman_ford(grafo, origem):
    """Retorna distâncias apenas aos vértices alcançáveis a partir de origem.

    O grafo tem formato {v: [(w, peso), ...]}, como em Dijkstra. Vértices
    presentes apenas como destinos são aceitos. Levanta ValueError se um ciclo
    de peso negativo for alcançável a partir da origem. Não modifica o grafo.
    """
    vertices = {origem, *grafo}
    arestas = []
    for v, vizinhos in grafo.items():
        for w, peso in vizinhos:
            vertices.add(w)
            arestas.append((v, w, peso))

    dist = {origem: 0}
    for _ in range(len(vertices) - 1):
        alterou = False
        for v, w, peso in arestas:
            if v in dist and (w not in dist or dist[v] + peso < dist[w]):
                dist[w] = dist[v] + peso
                alterou = True
        if not alterou:
            break

    for v, w, peso in arestas:
        if v in dist and (w not in dist or dist[v] + peso < dist[w]):
            raise ValueError("o grafo possui ciclo negativo alcançável")
    return dist
