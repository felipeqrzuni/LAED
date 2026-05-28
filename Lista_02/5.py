# 5. Verificar se existe algum elemento que aparece ao menos k vezes na lista

V = [7, 1, 9, 1, 7, 3, 9, 2, 1, 6, 8, 3]

def k_repeticoes(V, k):
    elementos_verificados = set()

    for i in range(len(V)):
        num = V[i]

        if num in elementos_verificados:
            continue # pois já contamos ele antes.
        
        contador = 0

        for j in range(len(V)):
            if V[j] == num:
                contador += 1

        elementos_verificados.add(V[i])

        if contador >= k: # utilizando >= pois é "ao menos k" vezes.
            return True, num 

    return False
        
k = int(input("Digite o valor de k: "))
print(k_repeticoes(V, k))

# Tempo de execução O(n^2).