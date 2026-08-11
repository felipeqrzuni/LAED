from LDC import *

class Solucao:
    def Q9(self, p, k):
        # 9. Apresente um algoritmo que transforma uma lista duplamente encadeada em uma lista de
        # listas de tamanho k.
        L = []

        q = p

        while q:

            # primeiro nó da nova sublista:
            inicio = q

            contador = 1

            # percorre k elementos:
            while q.proximo and contador < k:
                q = q.proximo
                contador += 1

            # guarda o próximo bloco:
            proximo = q.proximo

            # encerra a sublista atual:
            q.proximo = None

            if proximo:
                proximo.anterior = None

            # coloca o início da sublista no vetor:
            L.append(inicio)

            # continua na próxima sublista:
            q = proximo

        return L

s = Solucao()

lista = ListaDuplamenteEncadeada()
lista._inserir([1, 3, 7, 10, 13, 18, 21, 27])

L = s.Q9(lista.cabeca, 2)

for p in L:
    q = p

    while q:
        print(q.valor, end=" ")

        q = q.proximo

    print()

# Tempo de execução: O algoritmo percorre cada elemento da lista uma única vez, dividindo-a em sublistas de tamanho aproximadamente k. 
# Portanto, o tempo de execução é O(n). O vetor de ponteiros possui aproximadamente n/k posições, logo o espaço adicional utilizado é O(n/k).