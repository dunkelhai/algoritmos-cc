"""Union-Find com compressão de caminho e união por rank."""


class UnionFind:
    def __init__(self, n):
        self.pai = list(range(n))
        self.rank = [0] * n
        self.componentes = n

    def encontra(self, x):
        while self.pai[x] != x:
            self.pai[x] = self.pai[self.pai[x]]
            x = self.pai[x]
        return x

    def une(self, a, b):
        ra, rb = self.encontra(a), self.encontra(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.pai[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.componentes -= 1
        return True

    def conectados(self, a, b):
        return self.encontra(a) == self.encontra(b)
