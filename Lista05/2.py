from LDC import *

class Solucao:
    def Q2(self, p, x, y):
        # 2. Localizar um elemento X na lista, modificar o seu valor para Y
        # e depois movê-lo para a sua posição correta.

        q1 = p
        q2 = None

        while q1 and q1.valor != x:
            q2 = q1
            q1 = q1.proximo

        if q1 is None: # significa que o nó com valor atribuído x não está na lista.
            return p

        # Removemos o nó de valor x da lista encadeada.
        # Casos: 1. O nó é o primeiro elemento da lista.
        if q2 is None:
            p = q1.proximo
            if p:
                p.anterior = None
        # 2. O nó está entre nós:
        else:
            q2.proximo = q1.proximo
            if q1.proximo:
                q1.proximo.anterior = q2

        # Atualizamos o valor do nó de X para Y:
        q1.valor = y
        q1.proximo = None
        q1.anterior = None

        # Se, após a remoção do nó em que q1 aponta, a lista ficar vazia, apenas retornamos q1:
        if p is None:
            return q1

        # Procuramos agora pela posição correta do nó atualizado:
        q3 = p
        q4 = None

        # O laço faz que o ponteiro pare exatamente no ponto correto. Se após o laço q3 ficar nulo,
        # isso significa que sua posição correta é como elemento mais à direita da lista (o último).
        while q3 and q3.valor < y:
            q4 = q3
            q4 = q3.proximo

        if q4 is None: # significa que a posição correta é no sendo o primeiro nó:
            q1.proximo = p
            p.anterior = q1
            p = q1

        # Posição correta é sendo o último nó da lista:
        elif q3 is None:
            q4.proximo = q1
            q1.anterior = q4

        # Se não for nenhum destes casos, a inserção ocorre entre q4 e q3:
        else:
            q4.proximo = q1
            q1.anterior = q4
            q1.proximo = q3
            q3.anterior = q1

        return p

s = Solucao()
lista = ListaDuplamenteEncadeada()
lista._inserir([3, 5, 9, 10, 15])

lista.cabeca = s.Q2(lista.cabeca, 5, 52)
lista.exibir()

# Tempo de execução: O(n). O algoritmo faz uma passagemp para localizar o elemento x na lista O(n)
# e outra passagem para encontrar a posição correta para o nó alterado. Ou seja: O(n) + O(n) = 2 * O(n),
# que, do ponto de vista assintótico, é O(n).