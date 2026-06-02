import random

lista = [5, 8, 13, 2, 10, 1, 9, 7, 15, 27]

def Troca(lista, indice_um, indice_dois):
    lista[indice_um], lista[indice_dois] = lista[indice_dois], lista[indice_um]
    return lista

# Partição utilizando o esquema de lomuto:
def Particao(lista, inicio, fim):
    # Sorteando o pivô:
    posPivo = random.randint(inicio, fim)
    Troca(lista, posPivo, fim)
    pivo = lista[fim]
    i = inicio -1

    for idx in range(inicio, fim):
        if lista[idx] <= pivo:
            i += 1
            Troca(lista, i, idx)

    Troca(lista, i+1, fim) # Corrige o desvio do pivô.
    return i+1

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

def ParticaoBolha(lista):
    k = Particao(lista, 0, len(lista)-1)

    # Para o lado esquerdo:
    Bolha(lista, 0, k-1)
    
    # Para o lado direito:
    Bolha(lista, k+1, len(lista)-1)

    return lista

print(f"Antes: {lista}")
ParticaoBolha(lista)
print(f"Depois: {lista}")

# a) No melhor caso, o pivô consegue dividir a lista exatamente ao meio.
# A execução da bolha possui custo (n/2)^2. Somando, teremos: (n/2)^2 + (n/2)^2 = n^2/2
# A partição ocorre em O(n). Então: T(n) = O(n) + O(n^2/2) = O(n^2).

# b) No pior caso, o pivô fica em uma das extremidades, criando uma "sublista" de tamanho n-1.
# Neste caso, a função bolha terá custo O((n-1)^2) ~ O(n^2).

# Em ambos os casos, o tempo de execução será ~O(n^2).