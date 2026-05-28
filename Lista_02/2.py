# 2. Encontrar o k-ésimo maior elemento da lista

V = [9, 42, 21, 14, 25, 3, 19, 33, 45, 6]

def bubbleSort(V):
    for i in range(len(V)-1):
        if V[i] > V[i+1]:
            V[i], V[i+1] = V[i+1], V[i]

k = int(input(f"Digite o valor k (1-{len(V)}): "))

for i in range(len(V)): # Para ordenar a lista totalmente.
    bubbleSort(V)

print(f"O {k}-ésimo maior elemento da lista é: {V[len(V)-k]}")

# Tempo de execução: O(n^2).