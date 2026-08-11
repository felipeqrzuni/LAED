from LDC import *

class Solucao:
    def Busca(self, L, x):
        # Procuramos primeiro qual sublista pode conter x.
        # Como todas as sublistas e todos os seus elementos
        # estão ordenados, podemos parar assim que encontrarmos
        # um elemento maior que x.

        for i in range(len(L)):

            q = L[i]

            while q:

                if q.valor == x:
                    return q

                # Como a lista está ordenada, se encontramos
                # um valor maior que x, x não está nesta sublista
                # nem nas próximas.
                if q.valor > x:
                    return None

                q = q.proximo

        return None

    def Insercao(self, L, x):
        # Procuramos a sublista onde x deve ficar.
        i = 0

        while i < len(L) - 1:

            # Se o primeiro elemento da próxima sublista
            # já for maior que x, x deve ficar na sublista atual:
            if L[i + 1] is not None and L[i + 1].valor > x:
                break

            i += 1

        q = L[i]

        # Caso a sublista esteja vazia:
        if q is None:
            novo = Node(x)
            L[i] = novo
            return


        # Criamos o novo nó.
        novo = Node(x)


        # Caso x seja menor que o primeiro elemento:
        if x < q.valor:

            novo.proximo = q
            novo.anterior = None

            q.anterior = novo

            L[i] = novo

            return


        # Procuramos a posição correta dentro da sublista:
        while q.proximo and q.proximo.valor < x:
            q = q.proximo


        # Inserimos o novo nó depois de q:
        novo.proximo = q.proximo
        novo.anterior = q

        if q.proximo:
            q.proximo.anterior = novo

        q.proximo = novo

    def Remocao(self, L, x):

        # Procuramos a sublista que pode conter x:
        for i in range(len(L)):

            q = L[i]

            while q:
                if q.valor == x:

                    # Se q não é o primeiro elemento da sublista.
                    if q.anterior:
                        q.anterior.proximo = q.proximo

                    # Se q é o primeiro elemento da sublista,
                    # precisamos atualizar o ponteiro de L.
                    else:
                        L[i] = q.proximo

                    # Se existe um elemento depois de q,
                    # atualizamos seu ponteiro anterior.
                    if q.proximo:
                        q.proximo.anterior = q.anterior
                    return q

                # Como está ordenado, se passamos de x,
                # podemos parar.
                if q.valor > x:
                    return None

                q = q.proximo

        return None

    # Exibindo listas de listas:
    def Exibir(self, L):

            for i in range(len(L)):

                q = L[i]

                print(f"L[{i}] -> ", end="")

                while q:

                    print(q.valor, end="")

                    if q.proximo:
                        print(" <-> ", end="")

                    q = q.proximo

                print()
s = Solucao()
lista = ListaDuplamenteEncadeada()
lista._inserir([2, 9, 15, 19, 31, 49])
k = 2
L = []
q = lista.cabeca

while q:

    # Primeiro elemento da sublista atual
    inicio = q

    contador = 1

    # Percorre k elementos
    while q.proximo and contador < k:
        q = q.proximo
        contador += 1

    # Guarda o primeiro elemento da próxima sublista
    proximo = q.proximo

    # Desconecta a sublista atual da próxima
    q.proximo = None

    if proximo:
        proximo.anterior = None

    # Guarda o ponteiro para o início da sublista
    L.append(inicio)

    # Continua na próxima sublista
    q = proximo


print("LISTA INICIAL:")
s.Exibir(L)

# Para a busca:
print("\nBUSCA:")
x = 19
resultado = s.Busca(L, x)
if resultado:
    print(f"{x} encontrado.")
else:
    print(f"{x} não encontrado.")


x = 20
resultado = s.Busca(L, x)
if resultado:
    print(f"{x} encontrado.")
else:
    print(f"{x} não encontrado.")

# Para a inserção:
print("\nINSERÇÃO:")
x = 17
s.Insercao(L, x)
print(f"Depois de inserir {x}:")
s.Exibir(L)

# Para a remoção:
print("\nREMOÇÃO:")
x = 19
resultado = s.Remocao(L, x)
if resultado:
    print(f"{x} removido.")
else:
    print(f"{x} não encontrado.")
s.Exibir(L)

# Tempo de execução:
# Para a busca: O(m+k), onde m é o número de sublistas e k o tamanho de cada sublista (aproximadamente).
# Inserção:
# O(m + k) = O(n/k + k)
# Remoção:
# O(m + k) = O(n/k + k)