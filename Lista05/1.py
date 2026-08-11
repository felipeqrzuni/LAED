from LDC import *

class Solucao:
    def Q1(self, p):
        # 1. Imprimir o elemento central da lista.
        q1 = p
        q2 = p

        # Caminhamos pela lista encadeada com os dois ponteiros q1 e q2.
        # Encontramos o elemento central da lista fazendo q1 andar dois nós a frente de q2. Ou seja,
        # quando q1 estiver apontando para o último nó, q2 estará apontando exatamente para o nó do meio.
        # Então basta imprimirmos o valor relacionado ao nó em que q2 aponta.]

        while q1 and q1.proximo:
            q1 = q1.proximo.proximo
            q2 = q2.proximo

        print(q2.valor)
        return q2

s = Solucao()
lista = ListaDuplamenteEncadeada()
lista._inserir([3, 9, 5, 2, 8])

s.Q1(lista.cabeca)

# Tempo de execução: O(n), pois cada nó é visitado no máximo uma vez pelo ponteiro mais rápido q1.