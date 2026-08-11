from LDC import *

class Solucao:
   def Q4(self, p, k):
        # Implementação do algoritmo de partição:
        q = p
        r = p

        # Faz com que o ponteiro r aponte para o último objeto nó da lista.
        while r.proximo:
            r = r.proximo

        while q is not r and q.anterior is not r:

            # o ponteiro q procura por um elemento maior que k:
            while q is not r and q.anterior is not r and q.valor <= k:
                q = q.proximo

            # O ponteiro r procura por um elemento menor ou igual a k:
            while q is not r and q.anterior is not r and r.valor > k:
                r = r.anterior

            # No caso em que os ponteiros já se encontraram ou se cruzaram:
            if q is r or q.anterior is r:
                break

            # Troca os valores dos nós:
            q.valor, r.valor = r.valor, q.valor

            q = q.proximo
            r = r.anterior
        return p

s = Solucao()
lista = ListaDuplamenteEncadeada()
lista._inserir([9, 2, 5, 6, 1])
k = 5

lista.cabeca = s.Q4(lista.cabeca, k)
lista.exibir()

# Tempo de execução: O(n). Q percorre a lista da esquerda para a direita e r percorre a lista da direita para a esquerda.
# Cada nó é visitado no máximo algumas vezes, mas não temos um while completo dentro de outro que percorra novamente toda a lista.