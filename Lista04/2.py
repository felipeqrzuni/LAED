from LC import *

class Solucao:
    def Q2(self, p):
        # 2. Separar os elementos pares e ímpares em listas diferentes.

        lista_impar = ListaSimplesmenteEncadeada()
        lista_par = ListaSimplesmenteEncadeada()

        p1 = lista_impar.cabeca
        p2 = lista_par.cabeca

        q1 = p

        # Enquanto o elemento da lista atual não for nulo, checamos sua paridade
        # e inserimos na lista correspondente:
        while q1:
            if q1.valor % 2 == 0:
                lista_par.inserir(q1.valor)
                q1 = q1.proximo
            else:
                lista_impar.inserir(q1.valor)
                q1 = q1.proximo

        return (lista_impar, lista_par)


s = Solucao()

lista = ListaSimplesmenteEncadeada()
lista._inserir([2, 8, 5, 10, 7])

print("Lista antes:", end=" ")
lista.exibir()

(p1,p2) = s.Q2(lista.cabeca)

print("Após: ")
p1.exibir()
p2.exibir()

# Tempo de execução: O(n). Será necessário checar a paridade de todos os elementos
# para separá-los em suas respectivas listas encadeadas.