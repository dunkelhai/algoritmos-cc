"""Busca em profundidade e detecção de ciclo em grafo dirigido."""


def dfs(grafo, origem):
    visitados, ordem = set(), []

    def visita(v):
        visitados.add(v)
        ordem.append(v)
        for w in grafo.get(v, []):
            if w not in visitados:
                visita(w)

    visita(origem)
    return ordem


def tem_ciclo(grafo):
    BRANCO, CINZA, PRETO = 0, 1, 2
    cor = {v: BRANCO for v in grafo}

    def visita(v):
        cor[v] = CINZA
        for w in grafo.get(v, []):
            if cor.get(w, BRANCO) == CINZA:
                return True
            if cor.get(w, BRANCO) == BRANCO and visita(w):
                return True
        cor[v] = PRETO
        return False

    return any(cor[v] == BRANCO and visita(v) for v in list(grafo))
