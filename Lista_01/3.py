# 3. Procurar o número k na lista L e se ele não estiver lá, retornar 
# o elemento da lista com o valor mais próximo de k.

L = [9, 42, 21, 14, 25, 3, 19, 33, 45, 6]

def buscaAproximada(L, k):
    diferenca = None
    menorDiferenca = None
    elemMenorDiferenca = None
    
    for elemento in L:
        diferenca = abs(elemento - k)
        if diferenca == 0:
            return elemento
        elif menorDiferenca is None or diferenca < menorDiferenca:
            menorDiferenca = diferenca
            elemMenorDiferenca = elemento

    return menorDiferenca, elemMenorDiferenca

print(buscaAproximada(L, 52))
 
# O output neste caso será (7, 45), indicando que o elemento
# mais próximo do 52 é o 45, com uma distância de 7 unidades.
# Tempo de execução O(n).