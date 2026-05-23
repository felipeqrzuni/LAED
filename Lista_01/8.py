# 8. Imprimir todos os números que aparecem nas duas listas.


U = [9, 2, 7, 7, 2, 2, 1, 7, 7, 9]
V = [2, 15, 19, 12, 33, 9, 17, 41, 54, 8]

def intersecao(U,V):
    ocorrencias = set()
    for i in range(len(U)):
        num = U[i]
        for j in range(len(V)):
            if U[i] == V[j]:
                if num in ocorrencias:
                    continue
                else:
                    print(f"{num}")
                    ocorrencias.add(num)


intersecao(U,V)
