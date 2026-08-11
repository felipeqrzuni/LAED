from LC import *

class Solucao:
    def Q10(self, p1, p2):
        # 10. Construir uma terceira lista que contém todos os elementos que aparecem em ambas as listas.

        q1 = p1
        q2 = p2
        lista_resultante = ListaSimplesmenteEncadeada()

        # Para cada elemento da lista em que q1 aponta, procuramos um valor igual na lista em que q2 aponta.
        # Em caso afirmativo, inserimos este valor na lista resultante, e movemos novamente o ponteiro para
        # o começo da lista encadeada em que q2 deve apontar e avançamos o ponteiro q1 para o próximo elemento
        # da primeira lista.

        while q1:
            q2 = p2
            while q2:
                if q1.valor == q2.valor:
                    lista_resultante.inserir(q1.valor)
                    break
                else:
                    q2 = q2.proximo
            q1 = q1.proximo

        return lista_resultante

s = Solucao()
p1 = ListaSimplesmenteEncadeada()
p2 = ListaSimplesmenteEncadeada()

p1._inserir([3, 9, 2, 6, 4])
p2._inserir([4, 5, 2, 9, 3])

p3 = ListaSimplesmenteEncadeada()
p3 = s.Q10(p1.cabeca, p2.cabeca)
p3.exibir()

# Tempo de execução: O(n^2). Como são duas listas e para cada elemento de uma precisaremos caminhar na outra novamente
# para verificar se o valor repete. São n ações para cada elemento, portanto n^2. Estou levando em consideração o fato
# de ambas as listas possuirem aproximadamente o mesmo tamanho (~n).