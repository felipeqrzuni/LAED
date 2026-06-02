matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 2, 3]
]

linhas = len(matriz)
colunas = len(matriz[0])

for i in range(linhas):
    for j in range(i + 1, linhas):

        iguais = True

        for k in range(colunas):
            if matriz[i][k] != matriz[j][k]:
                iguais = False
                break

        if iguais:
            print(f"Linhas {i} e {j} são iguais")

# Tempo de execução: O(n^2 * m), e, se a matriz for quadrada, O(n^3).