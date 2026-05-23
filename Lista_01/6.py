# 6. Encontrar os dois elementos da lista L que possuem a menor diferença entre si (em valor absoluto).

V = [9, 2, 7, 7, 2, 2, 1, 7, 7, 9]

def dois_elementos_mais_proximos(V):
    diferenca = None
    menorDiferenca = None
    elemento_um = None
    elemento_dois = None

    for i in range(len(V)):
        for j in range (i+1, len(V)):
            diferenca = abs(V[i] - V[j])
            if menorDiferenca is None or diferenca < menorDiferenca:
                menorDiferenca = diferenca
                elemento_um = V[i]
                elemento_dois = V[j]
    return menorDiferenca, elemento_um, elemento_dois


print(dois_elementos_mais_proximos(V))


