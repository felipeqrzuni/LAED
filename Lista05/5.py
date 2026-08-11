from LDC_VE import *

class Solucao:
    def Q5(self, V):
        # 5. Apresente um algoritmo que constrói a representação de um vetor esparso na
        # forma de uma lista duplamente encadeada.
        lista = ListaDuplamenteEncadeada()
        i = 0
        tam = len(V)

        for i in range(tam):
            if V[i] == 0:
                continue
            else:
                lista.inserir(V[i], i)

        return lista

s = Solucao()
V = [0, 3, 0, 0, 0, 5, 0, 2, 0, 0, 8, 0, 0, 7, 0]
(s.Q5(V)).exibir()

# Tempo de execução: O(n). Será necessário percorrer todos os elementos da lista apenas uma única vez para 
# criar a lista duplamente encadeada.