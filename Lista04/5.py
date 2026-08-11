from LC import *

class Solucao:
    def Q5(self, p1, p2):
        # 5. Combinar os elementos das duas listas para produzir uma única lista ordenada.

        q1 = p1
        q2 = p2

        lista = ListaSimplesmenteEncadeada()
        p = lista.cabeca
        q = lista.cabeca

        # Enquanto ambas as listas não forem nulas, fazemos a comparação entre os valores atribuídos aos nós
        # em que os ponteiros q1 e q2 apontam. Se o valor atribuído ao nó em que q1 aponta for menor que o valor
        # atribuído ao nó em que q2 aponta, iremos inserir na nova lista encadeada um novo nó cujo valor atribuído será de q1. 
        # Mesma coisa ocorre analogamente caso o nó de menor valor atribuído seja q2.

        while q1 and q2:
            if q1.valor <= q2.valor:
                lista.inserir(q1.valor)
                q1 = q1.proximo
            elif q2.valor < q1.valor:
                lista.inserir(q2.valor)
                q2 = q2.proximo

        # A partir do instante em que uma das duas listas se tornam nulas, atribuímos a nova lista criada
        # o resto dos nós restantes da lista correspondente, seja ela a lista em que q1 aponta ou q2.

        while q1:
            lista.inserir(q1.valor)
            q1 = q1.proximo
        while q2:
            lista.inserir(q2.valor)
            q2 = q2.proximo

        return lista

s = Solucao()
p1 = ListaSimplesmenteEncadeada()
p2 = ListaSimplesmenteEncadeada()

p1._inserir([3, 6, 7, 10, 13])
p2._inserir([2, 4, 9, 11, 12])

lista = s.Q5(p1.cabeca, p2.cabeca)
lista.exibir()

# Tempo de execução O(n), onde n é o número de elementos da maior lista. Se ambas as listas possuírem o mesmo
# número de nós, apenas o primeiro while será rodado. Como constantes não afetam a nível assintótico o tempo
# de execução do algoritmo, dizemos que ele será O(n).