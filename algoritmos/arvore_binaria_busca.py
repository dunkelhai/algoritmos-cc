"""Árvore binária de busca (BST) sem balanceamento."""


class _No:
    def __init__(self, chave):
        self.chave = chave
        self.esq = None
        self.dir = None


class ArvoreBinariaBusca:
    def __init__(self):
        self._raiz = None

    def insere(self, chave):
        if self._raiz is None:
            self._raiz = _No(chave)
            return
        atual = self._raiz
        while True:
            if chave < atual.chave:
                if atual.esq is None:
                    atual.esq = _No(chave)
                    return
                atual = atual.esq
            elif chave > atual.chave:
                if atual.dir is None:
                    atual.dir = _No(chave)
                    return
                atual = atual.dir
            else:
                return

    def contem(self, chave):
        atual = self._raiz
        while atual:
            if chave == atual.chave:
                return True
            atual = atual.esq if chave < atual.chave else atual.dir
        return False

    def em_ordem(self):
        resultado, pilha, atual = [], [], self._raiz
        while pilha or atual:
            while atual:
                pilha.append(atual)
                atual = atual.esq
            atual = pilha.pop()
            resultado.append(atual.chave)
            atual = atual.dir
        return resultado

    def altura(self):
        def h(no):
            return 0 if no is None else 1 + max(h(no.esq), h(no.dir))
        return h(self._raiz)
