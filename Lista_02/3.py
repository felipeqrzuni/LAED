# 3. Encontre o elemento mais próximo da média aritmética da lista

V = [9, 42, 21, 14, 25, 3, 19, 33, 45, 6]

def mais_proximo_da_media(V):
    soma = 0
    media = 0
    diferenca = None
    menor_diferenca = None
    elemento = None

    for i in range(len(V)):
        soma += V[i] # O(n)
    media = soma/len(V)

    for i in range(len(V)): # O(n)
        diferenca = abs(V[i] - media)
        if menor_diferenca is None or diferenca < menor_diferenca:
            menor_diferenca = diferenca
            elemento = V[i]
        else:
            continue

    return menor_diferenca, elemento, media

resultado = mais_proximo_da_media(V)
print(f"{resultado[1]} (a média é {resultado[2]})")

# Tempo de execução: 2*O(n) = O(n).