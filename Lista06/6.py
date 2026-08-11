from PE import *

class FilaComDuasPilhas():
    def __init__(self):
        self.p1 = PilhaEncadeada()  # pilha de entrada
        self.p2 = PilhaEncadeada()  # pilha de saída

    def enqueue(self, valor):
        # (a) A inserção sempre empilha em P1, sem nenhum custo extra.
        self.p1.push(valor)

    def dequeue(self):
        # (a) A remoção retira o topo de P2. Se P2 estiver vazia, transferimos todos
        # os elementos de P1 para P2 antes de remover. Como P1 é LIFO, transferir
        # seus elementos para P2 inverte a ordem: o elemento mais antigo de P1 (o
        # primeiro que foi inserido na fila) acaba no topo de P2, que é exatamente o
        # elemento que uma fila FIFO deveria remover primeiro.
        if self.p2.estaVazia():
            while not self.p1.estaVazia():
                self.p2.push(self.p1.pop())

        return self.p2.pop()

    def exibir(self):
        print("P1 (entrada):", end=" ")
        self.p1.exibir()
        print("P2 (saída):", end=" ")
        self.p2.exibir()


class Solucao:
    def Q6(self):
        fila = FilaComDuasPilhas()

        fila.enqueue(1)
        fila.enqueue(2)
        fila.enqueue(3)

        print("Após Enqueue(1), Enqueue(2), Enqueue(3):")
        fila.exibir()

        removido = fila.dequeue()
        print(f"\nDequeue() removeu {removido} (P2 estava vazia, houve transferência P1 -> P2):")
        fila.exibir()

        fila.enqueue(4)
        removido = fila.dequeue()
        print(f"\nEnqueue(4) e depois Dequeue() removeu {removido} (P2 não estava vazia, não houve transferência):")
        fila.exibir()

s = Solucao()
s.Q6()

# (b) O custo amortizado de Dequeue é O(1), mesmo que uma chamada individual possa
# custar O(n) (quando P2 está vazia e é preciso transferir todos os elementos de
# P1). Usando o método do potencial, definimos Φ = número de elementos em P1
# (Φ >= 0 sempre, e Φ inicial = 0, então a soma dos custos amortizados nunca fica
# abaixo da soma dos custos reais, garantindo que a análise é válida).
#
#   Enqueue: o custo real é O(1) (um único Push em P1), e Φ aumenta em 1 (mais um
#   elemento em P1). Custo amortizado = custo real + ΔΦ = O(1) + O(1) = O(1).
#
#   Dequeue quando P2 não está vazia: custo real O(1) (um único Pop em P2), e Φ não
#   muda (P1 não é tocada). Custo amortizado = O(1) + 0 = O(1).
#
#   Dequeue quando P2 está vazia e P1 tem k elementos: o custo real é O(k) (k Pops
#   em P1 seguidos de k Pushes em P2) mais O(1) do Pop final em P2, ou seja O(k+1).
#   Mas Φ diminui em k (P1 perde seus k elementos), então ΔΦ = -k. Custo amortizado
#   = O(k+1) - k = O(1).
#
# Em todos os casos o custo amortizado é O(1); o custo real de O(n) de uma
# transferência é "pago antecipadamente" pelo potencial acumulado pelos n Enqueues
# anteriores que colocaram os elementos em P1.

# (c) Sim, a transferência de P1 para P2 preserva a propriedade FIFO. Exemplo:
# inserimos 1, 2, 3 nessa ordem (Enqueue(1), Enqueue(2), Enqueue(3)). Isso deixa
# P1 = topo -> 3 -> 2 -> 1 -> / (1 foi o primeiro a entrar na fila, e por isso está
# no fundo de P1). Ao transferir, cada Pop de P1 devolve, na ordem, 3, depois 2,
# depois 1, e cada um desses valores é empilhado em P2 nessa mesma ordem,
# resultando em P2 = topo -> 1 -> 2 -> 3 -> /. Agora 1 (o primeiro elemento
# inserido na fila) está no topo de P2 e será o primeiro a ser removido por
# Dequeue — exatamente o que uma fila FIFO exige. Isso acontece porque cada
# elemento é invertido duas vezes ao longo de sua vida (uma vez implicitamente ao
# ser empilhado em P1, outra ao ser movido para P2), e duas inversões devolvem a
# ordem original de chegada.
