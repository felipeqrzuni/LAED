# 2. Encontrar o segundo maior ímpar armazenado na lista (se ele existir)

V = [9, 42, 21, 14, 28, 3, 19, 32, 46, 6]

maiorImpar = None
segundoMaiorImpar = None

for elemento in V:
    if elemento % 2 != 0:
        if maiorImpar is None or elemento > maiorImpar:
            segundoMaiorImpar = maiorImpar
            maiorImpar = elemento


if segundoMaiorImpar is not None:
    print(f"O segundo maior número ímpar é: {segundoMaiorImpar}")
else:
    print("Não existem números ímpares na lista.")

# Tempo de execução O(n).