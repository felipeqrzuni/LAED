# 6. Verificar se as listas U e V são permutações uma da outra

U = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
V = [7, 2, 3, 1, 6, 5, 9, 10, 4, 8]

def perm(U, V):
    if len(U) != len(V):
        return False

    ocorrencias = set()
    for i in range(len(U)):
        num = U[i]

        if num not in ocorrencias:
            for j in range(len(V)):
                if V[j] == num:
                    ocorrencias.add(num)
                    break
    
    if len(ocorrencias) == len(U):
        return True

print(perm(U, V))

# Vale destacar que este algoritmo funciona apenas para listas que não possuem duplicatas.
# Tempo de execução: O(n^2).