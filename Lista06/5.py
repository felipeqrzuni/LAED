from PE import *

class Solucao:
    def Q5(self, expressao):
        # 5. Balanceamento de delimitadores.

        # Percorremos a expressão caractere a caractere. Sempre que encontramos um
        # abridor ((, [ ou {), empilhamos. Sempre que encontramos um fechador (), ]
        # ou }), verificamos se a pilha não está vazia e se o topo é o abridor
        # correspondente: se for, desempilhamos (o par foi casado corretamente); se
        # não for, a expressão é inválida. Ao final, a expressão só é válida se a
        # pilha tiver ficado vazia (todo abridor foi casado com um fechador).

        pares = {')': '(', ']': '[', '}': '{'}
        abridores = set(pares.values())

        pilha = PilhaEncadeada()

        for i, caractere in enumerate(expressao):
            if caractere in abridores:
                pilha.push(caractere)
            elif caractere in pares:
                if pilha.estaVazia():
                    return (False, i, caractere, "fechador sem abridor correspondente")

                topo = pilha.pop()

                if topo != pares[caractere]:
                    return (False, i, caractere, f"esperava fechar '{topo}', mas encontrou '{caractere}'")

        if not pilha.estaVazia():
            return (False, len(expressao), pilha.pop(), "abridor sem fechador correspondente")

        return (True, None, None, None)

s = Solucao()

expressoes = ["({[]})", "({[)}]", "({[]}[()]{})"]

for expressao in expressoes:
    (valida, posicao, caractere, motivo) = s.Q5(expressao)

    if valida:
        print(f"{expressao} -> válida.")
    else:
        print(f"{expressao} -> inválida na posição {posicao} (caractere '{caractere}'): {motivo}.")

# (b) Tempo de execução: O(n), onde n é o comprimento da expressão. Cada caractere
# é examinado uma única vez, e cada operação de pilha usada (Push, Pop, estaVazia)
# é O(1). Espaço: O(n) no pior caso, quando todos os caracteres da expressão são
# abridores (por exemplo, uma expressão só com "(((((" empilharia todos eles).

# (c) Aplicando o algoritmo às cadeias do enunciado:
#   ({[]})       -> válida: cada abridor é fechado na ordem correta.
#   ({[)}]       -> inválida na posição 3 (caractere ')'): quando encontramos ')',
#                   o topo da pilha é '[' (empilhado por causa do '[' na posição 2),
#                   e ')' não é o fechador de '[', portanto o par está incorreto.
#   ({[]}[()]{}) -> válida: cada abridor também é fechado na ordem correta.
