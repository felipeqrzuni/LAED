class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None


class ListaDuplamenteEncadeada():
    def __init__(self):
        self.cabeca = None

    def inserir(self, valor):
        novoNode = Node(valor)

        if self.cabeca is None:
            self.cabeca = novoNode
            return

        atual = self.cabeca

        while atual.proximo:
            atual = atual.proximo

        atual.proximo = novoNode
        novoNode.anterior = atual

    def exibir(self):
        atual = self.cabeca

        while atual:
            print(atual.valor, end="<->")
            atual = atual.proximo

        print(None)

    def _inserir(self, list):
        for element in list:
            self.inserir(element)
