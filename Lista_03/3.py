import math

def mediana_duas_listas(U, V, iniU, fimU, iniV, fimV):
    n = fimU - iniU + 1

    if n == 1:
        return min(U[iniU], V[iniV])

    mU = U[math.floor((iniU+n)/2)]
    mV = V[math.floor((iniV+n)/2)]

    if mU == mV:
        return mU

    if mU < mV:
        return mediana_duas_listas(U, V, math.floor((iniU+n)/2), fimU, iniV, math.floor((iniV+n)/2))
    else:
        return mediana_duas_listas(U, V, iniU, math.floor((iniU+n)/2), math.floor((iniV+n)/2), fimV)

# Listas ordenadas de mesmo tamanho
U = [1, 3, 6, 7, 10]
V = [2, 4, 8, 9, 11]

resultado = mediana_duas_listas(U, V, 0, len(U) - 1, 0, len(V) - 1)

print("Mediana:", resultado)

# Tempo de execução: O(log_2(n)), pois, para cada passo, descartamos metade dos elementos.