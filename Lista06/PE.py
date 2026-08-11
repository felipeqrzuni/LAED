class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class PilhaEncadeada():
    def __init__(self):
        self.topo = None

    def push(self, valor):
        novoNode = Node(valor)

        # O novo nó sempre entra na frente da pilha: aponta para o antigo topo
        # e passa a ser o novo topo.
        novoNode.proximo = self.topo
        self.topo = novoNode

    def pop(self):
        if self.topo is None:
            return None

        # Guardamos o nó removido em uma variável auxiliar antes de mover o topo,
        # senão perderíamos a referência a ele.
        noRemovido = self.topo
        self.topo = self.topo.proximo
        noRemovido.proximo = None

        return noRemovido.valor

    def estaVazia(self):
        return self.topo is None

    def exibir(self):
        atual = self.topo

        print("topo", end=" ")
        while atual:
            print(atual.valor, end=" -> ")
            atual = atual.proximo

        print("/")

    def _inserir(self, list):
        # Empilhamos na ordem inversa para que o primeiro elemento da lista
        # recebida acabe no topo, reproduzindo o desenho "topo -> a -> b -> c -> /".
        for element in reversed(list):
            self.push(element)
