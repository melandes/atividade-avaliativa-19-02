def verifica_delimitadores(expr: str) -> bool:
    # Pilha para guardar os delimitadores de abertura encontrados
    pilha = []

    # Mapa: para cada fechador, qual abridor ele exige no topo da pilha
    pares = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    # Percorre cada caractere da expressão
    for ch in expr:
        # Se for um delimitador de abertura, empilha
        if ch in '([{':
            pilha.append(ch)

        # Se for um delimitador de fechamento, valida
        elif ch in ')]}':
            # Se não tem nada aberto, não pode fechar
            if not pilha:
                return False

            # Verifica se o topo da pilha é o par correto
            topo = pilha.pop()
            if topo != pares[ch]:
                return False

    # No final, se ainda sobrou algo aberto, está inválido
    return len(pilha) == 0


# ----------------------------
# Programa principal
# ----------------------------
expressao = input("Digite a expressão: ")

if verifica_delimitadores(expressao):
    print("Válido: delimitadores fechados na ordem correta.")
else:
    print("Inválido: delimitadores incorretos ou fora de ordem.")