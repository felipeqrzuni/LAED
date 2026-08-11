from LC import *

class Solucao:
    def Q3(self, p):
        # 3. Inverter a ordem dos elementos da lista:

        # Trabalharemos com os ponteiros ant, atual e prox: para cada elemento da lista encadeada,
        # atribuímos ao ponteiro prox o próximo elemento do elemento atual e fazemos o atributo próximo
        # do elemento atual receber o elemento anterior (apontado por ant). Após isso, caminhamos para o próximo
        # elemento através de atual = prox.

        ant = None
        atual = p

        while atual:
            prox = atual.proximo
            atual.proximo = ant
            ant = atual
            atual = prox

        return ant

s = Solucao()
lista = ListaSimplesmenteEncadeada()
lista._inserir([3, 2, 5, 9, 4])

print("Lista antes:", end=" ")
lista.exibir()

lista.cabeca = s.Q3(lista.cabeca)

print("Lista após:", end=" ")
lista.exibir()

# Tempo de execução: O(n). Para mover toda a lista é necessário percorrê-la por inteiro, alterando os parâmetros próximo de cada.