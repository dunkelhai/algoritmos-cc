"""Pilha LIFO baseada em lista."""


class Pilha:
    def __init__(self):
        self._itens = []

    def empilha(self, item):
        self._itens.append(item)

    def desempilha(self):
        if self.vazia():
            raise IndexError("pilha vazia")
        return self._itens.pop()

    def topo(self):
        if self.vazia():
            raise IndexError("pilha vazia")
        return self._itens[-1]

    def vazia(self):
        return not self._itens

    def __len__(self):
        return len(self._itens)


def parenteses_balanceados(texto):
    """Exemplo clássico de uso de pilha."""
    pares = {")": "(", "]": "[", "}": "{"}
    pilha = Pilha()
    for c in texto:
        if c in "([{":
            pilha.empilha(c)
        elif c in pares:
            if pilha.vazia() or pilha.desempilha() != pares[c]:
                return False
    return pilha.vazia()
