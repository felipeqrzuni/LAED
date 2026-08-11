from LC import *

class Solucao:
    def Q6(self, p, k):

        q1 = p
        lista_menor = ListaSimplesmenteEncadeada()
        lista_maior = ListaSimplesmenteEncadeada()

        # A ideia é criar duas listas encadeadas separadas e, para cada valor atribuído ao nó da lista encadeada
        # principal, se o valor atribuído for menor ou igual k, um novo nó será criado com este valor na lista lista_menor.
        # Caso contrário, será inserido na lista_maior. Após terminar o primeiro laço, apenas conectamos as duas listas encadeadas.
        
        while q1:
            if q1.valor <= k:
                lista_menor.inserir(q1.valor)
                q1 = q1.proximo
            else:
                lista_maior.inserir(q1.valor)
                q1 = q1.proximo

        cabeca_maior = lista_maior.cabeca

        while cabeca_maior:
            lista_menor.inserir(cabeca_maior.valor)
            cabeca_maior = cabeca_maior.proximo

        return lista_menor 

s = Solucao()
lista = ListaSimplesmenteEncadeada()
lista._inserir([9, 2, 5, 6, 1])
k = 5

resposta = s.Q6(lista.cabeca, k)
resposta.exibir()

# Tempo de execução: O(n). Primeio realizamos a separação e inserção nas listas correspondentes, o que leva n passos para completar.
# No pior caso, a lista lista_maior possui n elementos, significando que não existe na lista principal nenhum elemento menor ou igual a k.
# No melhor caso, o elemento k consegue separar a lista em n/2 elementos cada, mas ainda assim será, do ponto de vista assintótico, O(n)
# ao conectar as duas listas.