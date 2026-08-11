from LC import *

class Solucao:
    def Q8(self, p):
        # 8. Encontrar o elemento que aparece mais vezes na lista.
        maior = 0
        elemento = None

        # Para cada instância de elemento, entraremos em outro loop para verificar o número de vezes que ele
        # aparece. Se o número de ocorrências for maior que o maior já atribuído antes, o valor da variável
        # maior é atualizada e a variável elemento também será atualizada contendo o elemento que aparece mais vezes.

        q1 = p
        while q1:
            contador = 0
            q = p

            while q:
                if q.valor == q1.valor:
                    contador += 1
                q = q.proximo

            if contador > maior:
                maior = contador
                elemento = q1.valor

            q1 = q1.proximo

        print(f"{elemento} é o elemento que aparece mais vezes, com {maior} ocorrências.")
        return elemento

s = Solucao()
lista = ListaSimplesmenteEncadeada()
lista._inserir([8, 3, 8, 5, 8, 3])
s.Q8(lista.cabeca)

# Tempo de execução: O(n^2). Dada a estrutura do algoritmo, como, para cada iteração, estamos entrando em outro loop
# para checar o número de ocorrência, isso faz com que para cada elemento, n passos sejam feitos. Como existem n elementos,
# teremos n*n = n^2 passos. Portanto, O(n^2).