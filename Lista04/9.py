from LC import *

class Solucao:
    def Q9(self, p):
        # 9. Determinar se a lista contém algum elemento repetido ou não.
        q1 = p

        # Para cada elemento, entramos em um loop a partir do próximo elemento e caminhamos pela lista
        # procurando se algum elemento satisfaz a propriedade de possuir valor igual ao q1. Se sim, imprime
        # "Sim." e retorna 1. Senão, imprime "Não." e retorna 0.

        while q1:
            if q1.proximo is not None:
                q2 = q1.proximo
                while q2:
                    if q1.valor == q2.valor:
                        print("Sim.")
                        return 1
                    else:
                        q2 = q2.proximo
            q1 = q1.proximo

        print("Não.")
        return 0

s = Solucao()
lista = ListaSimplesmenteEncadeada()
lista._inserir([2, 9, 7, 4, 1]) 

s.Q9(lista.cabeca)

# Tempo de execução: O(n^2). Pelo mesmo argumento da questão anterior, para cada elemento, caminhamos pela
# lista a procura de outro elemento de igual valor. Isso significa que para cada elemento, andamos, no máximo, n passos.
# Como são n elementos, e cada elemento possui n passos, n*n = n^2. Portanto, o algoritmo possui tempo de execução O(n^2).