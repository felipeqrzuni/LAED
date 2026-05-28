# 1. Encontrar o maior número ímpar armazenado na lista (se houver algum)

V = [9, 42, 21, 14, 28, 3, 19, 32, 46, 6]

maiorImpar = None

for elemento in V:
    if elemento % 2 != 0:
        if maiorImpar is None or elemento > maiorImpar:
            maiorImpar = elemento

if maiorImpar is not None:
    print(f"O maior número ímpar é: {maiorImpar}")
else:
    print("Não existem números ímpares na lista.")

# Tempo de execução O(n).