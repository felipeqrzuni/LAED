# 1. Encontrar o terceiro maior elemento da lista

V = [9, 42, 21, 14, 25, 3, 19, 33, 45, 6]

def encontrar_terceiro_maior(V):
    maior = None
    segundo_maior = None
    terceiro_maior = None

    for i in range(len(V)):
        num = V[i]
        if maior is None or num > maior:
            terceiro_maior = segundo_maior
            segundo_maior = maior
            maior = num
        elif num > segundo_maior:
            terceiro_maior = segundo_maior
            segundo_maior = num
        elif num > terceiro_maior:
            terceiro_maior = num
    
    return terceiro_maior

print(encontrar_terceiro_maior(V))

# Tempo de execução O(n).