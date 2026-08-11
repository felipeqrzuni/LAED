class NodeMin:
    def __init__(self, valor, minimoAteAqui):
        self.valor = valor
        self.minimoAteAqui = minimoAteAqui
        self.proximo = None


class PilhaComMinimo():
    # (a) Estrutura de dados: cada nó guarda, além do valor, o campo
    # minimoAteAqui — o menor valor entre todos os elementos que estão da posição
    # deste nó para baixo (incluindo ele mesmo). Assim, o mínimo de toda a pilha
    # está sempre disponível em topo.minimoAteAqui, sem percorrer a pilha.

    def __init__(self):
        self.topo = None

    def push(self, valor):
        if self.topo is None:
            minimoAteAqui = valor
        else:
            minimoAteAqui = min(valor, self.topo.minimoAteAqui)

        novoNode = NodeMin(valor, minimoAteAqui)
        novoNode.proximo = self.topo
        self.topo = novoNode

    def pop(self):
        if self.topo is None:
            return None

        noRemovido = self.topo
        self.topo = self.topo.proximo
        noRemovido.proximo = None

        return noRemovido.valor

    def min(self):
        if self.topo is None:
            return None

        return self.topo.minimoAteAqui

    def estaVazia(self):
        return self.topo is None

    def exibir(self):
        atual = self.topo

        print("topo", end=" ")
        while atual:
            print(f"{atual.valor}(min={atual.minimoAteAqui})", end=" -> ")
            atual = atual.proximo

        print("/")


class Solucao:
    def Q4(self):
        pilha = PilhaComMinimo()

        # (c) Traçamos a sequência: Push(5), Push(3), Push(7), Push(1), Pop, Min.
        pilha.push(5)
        print("Após Push(5):", end=" ")
        pilha.exibir()

        pilha.push(3)
        print("Após Push(3):", end=" ")
        pilha.exibir()

        pilha.push(7)
        print("Após Push(7):", end=" ")
        pilha.exibir()

        pilha.push(1)
        print("Após Push(1):", end=" ")
        pilha.exibir()

        removido = pilha.pop()
        print(f"Após Pop (removeu {removido}):", end=" ")
        pilha.exibir()

        print(f"Min: {pilha.min()}")

s = Solucao()
s.Q4()

# (b) Pseudocódigo de Push, Pop e Min, todos O(1):
#
# Push(topo, valor):
#     novoNode.valor <- valor
#     se topo = nulo:
#         novoNode.minimoAteAqui <- valor
#     senão:
#         novoNode.minimoAteAqui <- min(valor, topo.minimoAteAqui)
#     novoNode.proximo <- topo
#     topo <- novoNode
#
# Pop(topo):
#     se topo = nulo:
#         retorna erro (pilha vazia)
#     noRemovido <- topo
#     topo <- topo.proximo
#     noRemovido.proximo <- nulo
#     retorna noRemovido.valor
#
# Min(topo):
#     se topo = nulo:
#         retorna erro (pilha vazia)
#     retorna topo.minimoAteAqui
#
# As três operações só leem/escrevem campos do nó do topo (Min e Push), ou no
# máximo desconectam o nó do topo (Pop), sem nenhum laço percorrendo a pilha,
# portanto as três são O(1).

# (c) Traço da execução (formato valor(min)):
#   Push(5) -> topo 5(min=5) -> /
#   Push(3) -> topo 3(min=3) -> 5(min=5) -> /
#   Push(7) -> topo 7(min=3) -> 3(min=3) -> 5(min=5) -> /
#   Push(1) -> topo 1(min=1) -> 7(min=3) -> 3(min=3) -> 5(min=5) -> /
#   Pop     -> remove 1, sobra topo 7(min=3) -> 3(min=3) -> 5(min=5) -> /
#   Min     -> 3 (lido diretamente de topo.minimoAteAqui)

# (d) Custo extra de memória: O(1) por nó (um campo minimoAteAqui a mais em cada
# nó), portanto O(n) no total para uma pilha com n elementos — a mesma ordem de
# grandeza de uma pilha encadeada comum, apenas com uma constante um pouco maior
# (mais um campo numérico por nó).
