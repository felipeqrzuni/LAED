from FE import *

class Solucao:
    def contraExemploPilha(self):
        # (a) Contra-exemplo concreto: considere apenas dois números de 2 dígitos,
        # 42 e 12, inseridos nessa ordem. O dígito menos significativo de ambos é 2.
        #
        # Com filas (FIFO), 42 entra primeiro na fila do dígito 2, e 12 entra depois.
        # Ao coletar, saem na mesma ordem em que entraram: 42, 12 — a ordem relativa
        # original entre eles foi preservada, que é exatamente a propriedade de
        # estabilidade de que o Radix Sort depende para os passos seguintes.
        #
        # Se usássemos uma pilha (LIFO) no lugar dessa fila, 42 (inserido primeiro)
        # ficaria no fundo, e 12 (inserido depois) ficaria no topo. Ao "coletar"
        # desempilhando, sairia primeiro 12 e depois 42 — a ordem relativa entre eles
        # foi invertida. Isso quebra a estabilidade: na passagem seguinte, o dígito
        # das dezenas depende de que números com o mesmo dígito das unidades
        # permaneçam na ordem em que chegaram (para que a passagem anterior continue
        # "valendo"), mas com pilhas essa ordem se perde a cada dígito empatado, e o
        # resultado final pode sair fora de ordem.

        print("(a) Entrada: 42, 12 (nessa ordem). Dígito das unidades igual (2) para ambos.")
        print("(a) Com filas (estável):   saem na ordem 42, 12 -> ordem relativa preservada.")
        print("(a) Com pilhas (instável): sairiam na ordem 12, 42 -> ordem relativa invertida.")

    def radixSort(self, numeros, numDigitos):
        # (b) Radix Sort usando 10 filas encadeadas (uma por dígito, de 0 a 9). Para
        # cada posição decimal, do dígito menos significativo para o mais
        # significativo, distribuímos cada número na fila correspondente ao seu
        # dígito naquela posição e depois recolhemos as filas em ordem (da fila 0 até
        # a fila 9), formando a nova sequência que será usada na próxima passagem.

        sequencia = list(numeros)

        for passagem in range(numDigitos):
            filas = [FilaEncadeada() for _ in range(10)]

            for numero in sequencia:
                digito = (numero // (10 ** passagem)) % 10
                filas[digito].enqueue(numero)

            print(f"\nPassagem {passagem + 1} (dígito na posição {passagem}, peso 10^{passagem}):")

            for d in range(10):
                if not filas[d].estaVazia():
                    print(f"  Fila {d}:", end=" ")
                    filas[d].exibir()

            sequencia = []

            for d in range(10):
                while not filas[d].estaVazia():
                    sequencia.append(filas[d].dequeue())

            print(f"  Sequência coletada após a passagem {passagem + 1}: {sequencia}")

        return sequencia

s = Solucao()

s.contraExemploPilha()

numeros = [481, 329, 143, 612, 937, 480, 256]
print("\n(b) Sequência original:", numeros)

resultado = s.radixSort(numeros, 3)

print("\n(b) Sequência final ordenada:", resultado)

# (c) Complexidade: para n strings (ou números) de comprimento fixo k sobre um
# alfabeto de tamanho sigma, cada passagem distribui os n elementos nas sigma
# filas (O(n)) e depois recolhe as sigma filas (O(n + sigma), pois é preciso
# visitar todas as sigma filas mesmo que algumas estejam vazias). Como existem k
# passagens (uma por posição), o tempo total do Radix Sort é O(k(n + sigma)).
# Quando sigma é uma constante (por exemplo, sigma = 10 para dígitos decimais),
# isso se reduz a O(kn).
#
# Comparando com o Merge Sort: ordenar n strings de comprimento k por comparação
# custa O(nk log n), pois cada uma das O(n log n) comparações entre duas strings
# pode custar até O(k) no pior caso (é preciso comparar caractere a caractere até
# encontrar uma diferença). Como o Radix Sort é O(kn), ele é assintoticamente
# melhor que o Merge Sort sempre que log n é maior que uma constante — ou seja,
# para n suficientemente grande o Radix Sort (O(kn)) vence o Merge Sort (O(kn log
# n)). A vantagem do Radix Sort é justamente evitar o fator log n; em troca, ele
# paga com a dependência de sigma (o tamanho do alfabeto) e com a exigência de que
# k seja fixo (ou conhecido de antemão), algo que o Merge Sort não precisa.
