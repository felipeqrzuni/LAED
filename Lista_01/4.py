# 4.Verificar se existe algum número ímpar que aparece um número ímpar de vezes

V = [9, 2, 7, 7, 2, 2, 1, 7, 7, 9]

def imparImpar(V):
    visitados = set()
    for i in range(len(V)):
        num = V[i]
        if num in visitados:
            continue
        if num % 2 != 0:
            contador = V.count(num)
            if contador % 2 != 0:
                print(f"O número {num} aparece {contador} vezes (ímpar).")
                return True
            visitados.add(num)
    print("Nenhum número aparece uma quantidade ímpar de vezes.")
    return False

imparImpar(V)

