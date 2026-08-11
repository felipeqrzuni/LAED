from LC import *

class Solucao:
    def Q4(self, p):
        # 4. Duplicar os elementos ímpares da lista.

        q1 = p
        while q1:
            if q1.valor % 2 != 0:
                prox = q1.proximo
                novo = Node(q1.valor)
                q1.proximo = novo
                novo.proximo = prox
                q1 = prox
            else:
                q1 = q1.proximo

        return p

s = Solucao()
lista = ListaSimplesmenteEncadeada()
lista._inserir([2, 7, 6, 3])
print("Lista antes:", end=" ")
lista.exibir()

lista.cabeca = s.Q4(lista.cabeca)

print("lista após:", end=" ")
lista.exibir()

# Tempo de execução: O(n). Será necessário percorrer toda a lista encadeada para procurar por elementos ímpares.