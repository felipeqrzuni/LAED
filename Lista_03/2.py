import math

lista = [5, 8, 13, 2, 10, 1, 9, 7, 15, 27]

def Troca(lista, indice_um, indice_dois):
    lista[indice_um], lista[indice_dois] = lista[indice_dois], lista[indice_um]
    return lista

def Bolha(lista, inicio, fim):
    houveTroca = False
    for idx in range(inicio, fim):
        if lista[idx] > lista[idx+1]:
            Troca(lista, idx, idx+1)
            houveTroca = True
        else:
            continue

    if houveTroca == True:
        Bolha(lista, inicio, fim)

doisTercos = math.floor(2*len(lista)/3)
umTerco = math.floor(len(lista)/3)

print("Lista antes da ordenação: ")
print(lista)
print("Ordenando 2n/3 primeiros: ")
Bolha(lista, 0, doisTercos-1)
print(lista)
print("Ordenando os últimos 2n/3: ")
Bolha(lista, umTerco, len(lista)-1)
print(lista)
print("Ordenando novamente os primeiros 2n/3: ")
Bolha(lista, 0, doisTercos-1)
print(lista)

# Lista antes da ordenação: 
# [5, 8, 13, 2, 10, 1, 9, 7, 15, 27]
# Ordenando 2n/3 primeiros: 
# [1, 2, 5, 8, 10, 13, 9, 7, 15, 27]
# Ordenando os últimos 2n/3: 
# [1, 2, 5, 7, 8, 9, 10, 13, 15, 27]
# Ordenando novamente os primeiros 2n/3: 
# [1, 2, 5, 7, 8, 9, 10, 13, 15, 27]

# a) Sim. A lista está completamente ordenada.
# Após a primeira etapa, os primeiros 2n/3 elementos estão ordenados entre si.
# Os últimos n/3 elementos ainda podem estar fora de ordem. Com isso,
# na segunda etapa, ordenamos os últimos 2n/3 elementos. Como essa região se
# "sobrepõem" à primeira em um intervalo n/3, elementos que estavam em posições
# incorretas próximas à "fronteira" entre os dois blocos podem ser deslocados
# para suas posições adequadas. Ao final dessa etapa, o último 2n/3 da lista
# está ordenado.

# No entanto, a segunda etapa pode ter alterado a ordem de alguns elementos da
# região inicial da lista. Por isso, realizamos uma terceira ordenação nos primeiros
# 2n/3 elementos. Novamente, como os dois blocos se "sobrepõem" em n/3 posições,
# essa última etapa corrige as inversões da parte inicial, sem alterar a ordenação
# da parte final (n/3).


# b) O custo da bolha é O(n^2), então:
# T(n) = O((2n/3)^2) + O((2n/3)^2) + O((2n/3)^2)
# => T(n) = O(3*(4n^2/9)) => T(n) = O(4n^2/3)
# que, do ponto de vista assintótico, é O(n^2).