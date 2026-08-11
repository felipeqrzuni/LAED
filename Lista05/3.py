from LDC import *

class Solucao:
    def Q3(self, p):
        # 3. Percorrer a lista da esquerda para a direita, trocando o elemento atual de posição com o próximo
        # quando este é menor do que aquele.

        q1 = p
        q2 = None

        while q1 and q1.proximo:
            # Se o sucessor de q1 existir e o valor atribuído ao nó de q1 for maior que o seu sucessor:
            if q1.valor > q1.proximo.valor:

                temp = q1.proximo

                # Se q1 estiver apontando para o primeiro nó da lista:
                if q2 is None:
                    q1.proximo = temp.proximo
                    if temp.proximo:
                        temp.proximo.anterior = q1

                    temp.anterior = None
                    temp.proximo = q1
                    q1.anterior = temp

                    p = temp

                else:
                    # Se q2 não é nulo, estamos apontando para um nó entre nós:
                    q1.proximo = temp.proximo
                    if temp.proximo:
                        temp.proximo.anterior = q1

                    temp.anterior = q2
                    q2.proximo = temp

                    temp.proximo = q1
                    q1.anterior = temp

                    # q2 passa a ser o nó que acabou de vir antes de q1.
                    q2 = temp

            else:
                q2 = q1
                q1 = q1.proximo

        return p

s = Solucao()
lista = ListaDuplamenteEncadeada()
lista._inserir([9, 3, 8, 5, 1])

lista.cabeca = s.Q3(lista.cabeca)
lista.exibir()

# Tempo de execução: O(n). A varredura passa no máximo uma vez por cada nó da lista. Para uma lista totalmente
# desordenada, executar a varredura n vezes ordenada a lista completamente, no entanto, ocorrerá em O(n^2).