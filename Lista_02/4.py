# 4. Verificar se a lista contém algum elemento isolado.

# def.: K é um elemento isolado se, somente se, os números k-1 e k+1 não estão na lista.

V = [17, 2, 8, 1, 7, 13, 9, 12, 4, 16]

def elemento_isolado(V):
    elemento_isolado_flag = None
    elementos_isolados = set()

    for i in range(len(V)):
        num = V[i]
        num_inferior = False 
        num_posterior = False 
        
        for j in range(len(V)):
            if V[j] == num-1:
                num_inferior = True
            elif V[j] == num+1:
                num_posterior = True
        if not num_inferior and not num_posterior:
            elementos_isolados.add(num)
    return elementos_isolados

print(elemento_isolado(V))

# Tempo de execução O(n^2).