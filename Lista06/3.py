from FE import *
from PE import *

class Solucao:
    def Q3(self, fila):
        # 3. Inversão de fila com pilha auxiliar.

        # A ideia é: enquanto a fila não estiver vazia, retiramos (Dequeue) cada
        # elemento da fila e empilhamos (Push) na pilha auxiliar. Como a pilha é LIFO,
        # o primeiro elemento retirado da fila (que estava em inicio) acaba no fundo
        # da pilha, e o último elemento retirado (que estava mais perto de fim) acaba
        # no topo. Em seguida, esvaziamos a pilha de volta para a fila: a cada Pop
        # (que devolve os elementos na ordem inversa à que entraram) fazemos um
        # Enqueue na fila original. Assim, o elemento que estava em fim volta a ser o
        # primeiro a ser reinserido, e o que estava em inicio volta por último —
        # invertendo a ordem original da fila.

        pilha = PilhaEncadeada()

        while not fila.estaVazia():
            pilha.push(fila.dequeue())

        while not pilha.estaVazia():
            fila.enqueue(pilha.pop())

        return fila

s = Solucao()

fila = FilaEncadeada()
fila._inserir([1, 2, 3, 4])

print("(a) Fila antes:", end=" ")
fila.exibir()

s.Q3(fila)

print("(a) Fila depois:", end=" ")
fila.exibir()

# (a) Traçando a execução para a fila <1, 2, 3, 4> (onde 1 está em inicio):
#
# Primeira etapa (fila -> pilha):
#   Dequeue() = 1, Push(1) -> pilha: topo -> 1 -> /
#   Dequeue() = 2, Push(2) -> pilha: topo -> 2 -> 1 -> /
#   Dequeue() = 3, Push(3) -> pilha: topo -> 3 -> 2 -> 1 -> /
#   Dequeue() = 4, Push(4) -> pilha: topo -> 4 -> 3 -> 2 -> 1 -> /
#
# Segunda etapa (pilha -> fila):
#   Pop() = 4, Enqueue(4) -> fila: inicio -> 4 -> / fim
#   Pop() = 3, Enqueue(3) -> fila: inicio -> 4 -> 3 -> / fim
#   Pop() = 2, Enqueue(2) -> fila: inicio -> 4 -> 3 -> 2 -> / fim
#   Pop() = 1, Enqueue(1) -> fila: inicio -> 4 -> 3 -> 2 -> 1 -> / fim
#
# Resultado: <4, 3, 2, 1>, exatamente a fila original invertida.

# (b) Tempo de execução: O(n). Cada elemento da fila passa por exatamente um
# Dequeue, um Push, um Pop e um Enqueue, todas operações O(1), logo o custo total é
# O(n). Espaço: O(n), pois a pilha auxiliar chega a armazenar todos os n elementos
# da fila simultaneamente (no pior caso, logo após a primeira etapa terminar).

# (c) Não é possível inverter a fila totalmente in-place, sem nenhuma variável
# auxiliar, usando apenas manipulação de ponteiros: em uma fila encadeada simples
# cada nó só tem o ponteiro proximo (aponta para frente, no sentido de inicio para
# fim), então para inverter a ordem lógica seria preciso inverter a direção de todos
# os proximo e trocar os papéis de inicio e fim — exatamente como se faz para
# inverter uma lista simplesmente encadeada (questão 3 da lista 04). Isso pode ser
# feito sem alocar nenhum nó novo e sem usar uma pilha (ou outra fila) auxiliar,
# percorrendo a fila apenas uma vez, mas ainda assim são necessárias variáveis
# auxiliares (ponteiros ant, atual, prox) para não perder a referência ao restante
# da fila enquanto os proximo são invertidos. Ou seja: dá para eliminar a estrutura
# auxiliar (a pilha), mas não dá para eliminar toda e qualquer variável auxiliar —
# "sem nenhuma estrutura auxiliar" e "sem nenhuma variável auxiliar" são coisas
# diferentes.
