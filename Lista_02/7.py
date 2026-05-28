# 7. Verificar se existem dois elementos repetidos que se encontram a uma distância de no máximo k um do outro.

V = [2, 1, 9, 7, 6, 3, 9, 4, 2, 6, 1, 3]

def repetidos_proximos(V, k):
    for i in range(len(V)):
        num = V[i]

        for j in range(i+1, len(V)):
            if V[i] == V[j] and j - i <= k:
                return True
    return False

k = int(input("Digite o valor de k: "))
print(repetidos_proximos(V, k))

# Tempo de execução: O(n^2).