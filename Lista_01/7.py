# 7. Contar o número de inversões na lista V

V = [9, 2, 7, 7, 2, 2,1, 7, 7, 9]

def num_inversoes(V):
    inversoes = 0
    total_inversoes = 0
    for i in range(len(V)):
        for j in range(i+1, len(V)):
            if V[i] > V[j]:
                inversoes += 1
        total_inversoes = total_inversoes + inversoes
        inversoes = 0
    return total_inversoes

print(num_inversoes(V))
