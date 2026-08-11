class Node:
    def __init__(self, valor, indice):
        self.valor = valor
        self.indice = indice
        self.proximo = None
        self.anterior = None


class ListaDuplamenteEncadeada():
    def __init__(self):
        self.cabeca = None

    def inserir(self, valor, indice):
        novoNode = Node(valor, indice)

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
            print(atual.valor, atual.indice, end="<->")
            atual = atual.proximo

        print(None)

    def _inserir(self, list):
        for element in list:
            self.inserir(element)