"""Fila FIFO usando duas pilhas (custo amortizado O(1))."""


class Fila:
    def __init__(self):
        self._entrada = []
        self._saida = []

    def enfileira(self, item):
        self._entrada.append(item)

    def desenfileira(self):
        self._transfere()
        if not self._saida:
            raise IndexError("fila vazia")
        return self._saida.pop()

    def frente(self):
        self._transfere()
        if not self._saida:
            raise IndexError("fila vazia")
        return self._saida[-1]

    def _transfere(self):
        if not self._saida:
            while self._entrada:
                self._saida.append(self._entrada.pop())

    def __len__(self):
        return len(self._entrada) + len(self._saida)
