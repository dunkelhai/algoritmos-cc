"""Lista simplesmente encadeada."""


class _No:
    __slots__ = ("valor", "proximo")

    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo


class ListaEncadeada:
    def __init__(self, valores=()):
        self._cabeca = None
        self._tamanho = 0
        for v in reversed(list(valores)):
            self.insere_inicio(v)

    def insere_inicio(self, valor):
        self._cabeca = _No(valor, self._cabeca)
        self._tamanho += 1

    def remove(self, valor):
        anterior, atual = None, self._cabeca
        while atual:
            if atual.valor == valor:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self._cabeca = atual.proximo
                self._tamanho -= 1
                return True
            anterior, atual = atual, atual.proximo
        return False

    def inverte(self):
        anterior, atual = None, self._cabeca
        while atual:
            atual.proximo, anterior, atual = anterior, atual, atual.proximo
        self._cabeca = anterior

    def __iter__(self):
        atual = self._cabeca
        while atual:
            yield atual.valor
            atual = atual.proximo

    def __len__(self):
        return self._tamanho
