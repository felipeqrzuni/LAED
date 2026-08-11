from FE import *

class Solucao:
    def Q2(self):
        # 2. Fila encadeada com ponteiros inicio e fim.

        # Construímos a fila inicial do enunciado: inicio -> 8 -> 15 -> 23 -> / fim
        fila = FilaEncadeada()
        fila._inserir([8, 15, 23])

        print("Estado inicial:", end=" ")
        fila.exibir()

        # (a) Inserimos os valores 7 e 11. Cada Enqueue cria um novo nó, conecta o
        # antigo fim a ele através do atributo proximo e atualiza fim para o novo nó.
        # O ponteiro inicio nunca é alterado por uma inserção.
        fila.enqueue(7)
        fila.enqueue(11)

        print("(a) Após Enqueue(7) e Enqueue(11):", end=" ")
        fila.exibir()

        # (b) Realizamos dois Dequeue. Cada Dequeue guarda o nó apontado por inicio em
        # uma variável auxiliar, avança inicio para inicio.proximo e retorna o valor
        # do nó guardado.
        removido1 = fila.dequeue()
        removido2 = fila.dequeue()

        print(f"(b) Primeiro Dequeue removeu: {removido1}")
        print(f"(b) Segundo Dequeue removeu: {removido2}")
        print("(b) Estado após os dois Dequeue:", end=" ")
        fila.exibir()

        # (c) Quando a última remoção esvazia a fila, inicio passa a apontar para
        # None (pois fizemos inicio = inicio.proximo, e o nó removido não tinha
        # próximo). Nesse momento é obrigatório também zerar fim (fim = None); caso
        # contrário fim continuaria apontando para o nó que acabamos de remover. 

s = Solucao()
s.Q2()

# Tempo de execução: Enqueue e Dequeue mexem apenas nos ponteiros inicio e/ou fim,
# sem percorrer a fila, portanto ambas são O(1). Construir a fila inicial com n
# elementos custa O(n), mas isso é só a preparação do cenário do enunciado.
