# 5.Verificar se existem dois elementos na lista L tais que um deles é dobro do outro.


L = [9, 42, 21, 14, 25, 3, 19, 33, 45, 6] #Vetor desordenado
V = [3, 6, 9, 14, 19, 21, 25, 33, 42, 45] #Vetor ordenado

def item_lista_desordenada(L):
    for i in range(len(L)):
        numero = L[i]
        for j in range(len(L)):
            if L[j] == 2*numero:
                print(f"Sim, os números {numero} e {L[j]} - lista desordenada.")
                return True
    return False

def item_lista_ordenada(V):
    for i in range(len(V)):
        numero = V[i]
        for j in range(i+1, len(V)):
            if V[j] == 2*numero:
                print(f"Sim, os números {numero} e {V[j]} - lista ordenada.")
                return True
    return False

item_lista_desordenada(L)
item_lista_ordenada(V)
