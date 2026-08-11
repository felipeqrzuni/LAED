from PE import *

class Solucao:
    def Q1(self):
        # 1. Operações básicas de pilha encadeada.

        # Construímos a pilha inicial do enunciado: topo -> 42 -> 17 -> 5 -> /
        pilha = PilhaEncadeada()
        pilha._inserir([42, 17, 5])

        print("Estado inicial:", end=" ")
        pilha.exibir()

        # (a) Executamos Push(topo, 99) e depois Push(topo, 3). Cada Push cria um novo
        # nó, faz o atributo proximo dele apontar para o antigo topo e atualiza topo
        # para o novo nó. Por isso os valores mais recentes ficam sempre na frente da
        # pilha, e o desenho passa a ser: topo -> 3 -> 99 -> 42 -> 17 -> 5 -> /
        pilha.push(99)
        pilha.push(3)

        print("(a) Após Push(99) e Push(3):", end=" ")
        pilha.exibir()

        # (b) A partir do estado obtido em (a), realizamos dois Pop. Cada Pop guarda o
        # nó apontado por topo em uma variável auxiliar, avança topo para topo.proximo
        # e só então desconecta o nó guardado, retornando seu valor.
        removido1 = pilha.pop()
        removido2 = pilha.pop()

        print(f"(b) Primeiro Pop removeu: {removido1}")
        print(f"(b) Segundo Pop removeu: {removido2}")
        print("(b) Estado após os dois Pop:", end=" ")
        pilha.exibir()

        # (c) O Pop precisa guardar o nó removido em uma variável auxiliar antes de
        # avançar o ponteiro topo porque, assim que topo passa a apontar para o nó
        # seguinte, perdemos a única referência que existia ao nó antigo: em uma pilha
        # encadeada só existem ponteiros indo do topo em direção à base, nenhum nó
        # aponta de volta para quem está acima dele. Se o nó fosse liberado da memória
        # imediatamente, antes de atualizarmos topo, o próprio ponteiro topo passaria
        # a apontar para um endereço de memória já desalocado. Qualquer tentativa de ler topo.valor ou topo.proximo
        # depois disso acessaria memória inválida, causando comportamento indefinido.

s = Solucao()
s.Q1()

# Tempo de execução: cada operação Push e Pop mexe apenas no nó do topo, sem
# percorrer o restante da pilha, portanto ambas são O(1). Construir a pilha inicial
# com n elementos custa O(n), mas isso é só a preparação do cenário do enunciado,
# não faz parte das operações Push/Pop em si.
