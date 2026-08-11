from LC import *

class Solucao:
    def Q7(self, p, k):
        # 7. Remover da lista todas as cópias de um certo elemento k (incluindo o próprio k).

        q1 = p
        q2 = None

        # Caminhamos pela lista, e para cada elemento repetido (condição q1.valor == k), fazemos o atributo
        # proximo do nó anterior apontar para o mesmo nó em que o atributo proximo do nó atual aponta. Em seguida,
        # fazemos o atributo proximo do nó atual apontar para nulo e caminhamos pela lista: q1 = q2.proximo.

        while q1:
            if q1.valor == k:
                q2.proximo = q1.proximo
                q1.proximo = None
                q1 = q2.proximo
            else:
                q2 = q1
                q1 = q1.proximo

        return p

s = Solucao()
lista = ListaSimplesmenteEncadeada()
lista._inserir([1, 3, 3, 2, 3, 2])

lista.cabeca = s.Q7(lista.cabeca, 3)
lista.exibir()

# Tempo de execução: O(n). O laço permanecerá atuando até não houver mais nós para avaliar na lista.
# Para cada nó com valor atribuído k, ordenamos os atributos proximo do nó anterior para apontar para o
# sucessor do nó atual (k).