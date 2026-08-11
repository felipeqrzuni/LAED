from LC import *

class Solucao:
    # 1. Localizar o maior elemento da lista e movê-lo para a última posição.
    def Q1(self, p):
        q1 = p
        q2 = None
        maior = None
        ant_ao_maior = None

        # Os ponteiros q1 e q2 irão andar juntos, q2 estando sempre um nó
        # atrás de q1. Queremos que exista um ponteiro que aponte para o maior
        # e para seu antecessor (anterior_ao_maior). Após encontrarmos o maior,
        # fazemos o nó atributo próximo do nó ant_ao_maior receber o próximo do maior.
        # Por fim, fazemos o atributo próximo de q2 (que é o último nó) apontar para o maior,
        # e o proximo do maior apontar para nulo.

        while q1:
            if maior is None or q1.valor > maior.valor:
                maior = q1
                ant_ao_maior = q2
            q2 = q1
            q1 = q1.proximo

        # Casos:

        # 1. Se ant_ao_maior for nulo, isso implica que o maior elemento é o primeiro nó da lista encadeada:
        # fazemos o ponteiro p apontar para o próximo nó, q2.proximo apontar para o maior e maior.proximo para nulo

        if ant_ao_maior is None:
            p = maior.proximo
            q2.proximo = maior
            maior.proximo = None

        # 2. O maior elemento estiver entre nós, fazemos o ant_ao_maior.proximo receber o maior.proximo,
        # q2.proximo receber o maior, e o maior apontar para nulo.

        elif ant_ao_maior is not None and maior.proximo is not None:
            ant_ao_maior.proximo = maior.proximo
            q2.proximo = maior
            maior.proximo = None

        # 3. Se não for nenhum dos casos anteriores, o maior elemento é o último nó da lista encadeada, portanto
        # q2 = maior:
        if maior == q2:
            return p

s = Solucao()
lista = ListaSimplesmenteEncadeada()

# Criamos uma lista encadeada:
lista._inserir([5, 8, 13, 2, 10])
# Definimos p como o ponteiro que aponta para o primeiro elemento da lista:
p = lista.cabeca

# Lista antes:
print("Lista original:", end=" ")
lista.exibir()

s.Q1(p)

# Lista após:
print("Lista modificada:", end=" ")
lista.exibir()

# Tempo de execução do algoritmo: independentemente será O(n), visto que será necessário
# percorrer toda a lista encadeada para procurar pelo maior, fazer o último elemento apontar
# para o maior. Mesmo o maior elemento sendo o primeiro, da lista ou o último, o algoritmo será O(n).