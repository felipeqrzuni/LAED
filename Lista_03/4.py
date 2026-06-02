import numpy
import random

matriz = numpy.random.randint(0, 10, size=(3,3))
linhas = len(matriz)
colunas = len(matriz[0])
visitados = set()

for i in range(linhas):
    for j in range(colunas):
        valor = matriz[i][j]
        
        if valor in visitados:
            print(f"Valor repetido encontrado: {valor}")
        else:
            visitados.add(valor)

# Também poderia utilizar a seguinte versão. No entanto, ela possui complexidade O(n^4) para matrizes quadradas.
#
# for i in range(linhas):
#     for j in range(colunas):
#         for k in range(linhas):
#             for l in range(colunas):
# 
#                 if (i != k or j != l) and matriz[i][j] == matriz[k][l]:
#                     print(f"Valor repetido: {matriz[i][j]}")