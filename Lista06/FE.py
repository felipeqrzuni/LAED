class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class FilaEncadeada():
    def __init__(self):
        self.inicio = None
        self.fim = None

    def enqueue(self, valor):
        novoNode = Node(valor)

        if self.fim is None:
            # Fila vazia, o novo nó é ao mesmo tempo inicio e fim.
            self.inicio = novoNode
            self.fim = novoNode
            return

        self.fim.proximo = novoNode
        self.fim = novoNode

    def dequeue(self):
        if self.inicio is None:
            return None

        # Guardamos o nó removido em uma variável auxiliar antes de mover inicio,
        # pelo mesmo motivo do Pop da pilha.
        noRemovido = self.inicio
        self.inicio = self.inicio.proximo

        # Se a fila ficou vazia após a remoção, fim também precisa ser zerado,
        # senão ficaria apontando para um nó que já não pertence mais à fila.
        if self.inicio is None:
            self.fim = None

        noRemovido.proximo = None

        return noRemovido.valor

    def estaVazia(self):
        return self.inicio is None

    def exibir(self):
        atual = self.inicio

        print("inicio", end=" ")
        while atual:
            print(atual.valor, end=" -> ")
            atual = atual.proximo

        print("/ fim")

    def _inserir(self, list):
        for element in list:
            self.enqueue(element)
