from LDC_VE import *

class Solucao:
    # 6. Implementação das funções busca_por_indice(k), # busca_por_valor(x), # atualização(x, k).
    def busca_por_indice(self, p, k):
        if p is None:
            print("Lista vazia.")
            return -1

        q = p

        while q:
            if q.indice == k:
                return q.valor
            q = q.proximo

        print(f"Elemento de índice {k} não existe na lista dada.")
        return -1

    def busca_por_valor(self, p, x):
        if p is None:
            print("Lista vazia.")
            return -1

        q = p
        while q:
            if q.valor == x:
                return q.indice
            q = q.proximo

        print(f"Elemento de valor {x} não existe na lista.")
        return -1

    def atualizacao(self, p, x, k):
        if p is None:
            print("Lista vazia.")
            return -1

        q = p
        while q:
            if q.indice == k:
                break
            q = q.proximo

        q.valor = x
        return p

s = Solucao()
lista = ListaDuplamenteEncadeada()
lista.inserir(4, 3) # <- (valor, indice)
lista.inserir(5, 7)
lista.inserir(10, 9)
lista.inserir(1, 12)
lista.inserir(9, 17)

print(s.busca_por_indice(lista.cabeca, 3)) # retorna 4
print(s.busca_por_valor(lista.cabeca, 10)) # retorna 9
lista.cabeca = s.atualizacao(lista.cabeca, 52, 17) # Troca o valor do índice 17 para 52.
lista.exibir()

# Tempo de execução O(n). Todos os algoritmos são em tempo linear pois cada nó é visitado apenas uma única vez.
# Seja para busca por indice, busca por elemento, ou atualização de um elemento dado o índice.
