# ==============================
# TOKENIZAÇÃO SIMPLES
# ==============================

# String fixa (poderia ser input do usuário)
expressao = "soma = 10 + 20 ;"

# ------------------------------------------------
# A função split() divide a string usando espaço
# como delimitador.
# Exemplo:
# "soma = 10" -> ["soma", "=", "10"]
# ------------------------------------------------
tokens = expressao.split()


# Conjunto de operadores matemáticos
operadores = {"+", "-", "*", "/"}

# Símbolo de atribuição
atribuicao = "="

# Símbolo de fim de instrução
fim_instrucao = ";"


# Percorre cada token da lista
for token in tokens:

    # ------------------------------------------------
    # isidentifier() verifica se o token é um nome válido
    # de variável (começa com letra ou _ e pode ter números)
    # ------------------------------------------------
    if token.isidentifier():
        print(f"{token} -> Identificador")

    # ------------------------------------------------
    # isdigit() verifica se o token é um número inteiro
    # (apenas dígitos)
    # ------------------------------------------------
    elif token.isdigit():
        print(f"{token} -> Número")

    # Verifica se o token está dentro do conjunto
    # de operadores definidos
    elif token in operadores:
        print(f"{token} -> Operador")

    # Verifica se é o símbolo de atribuição
    elif token == atribuicao:
        print(f"{token} -> Atribuição")

    # Verifica se é o símbolo de fim de instrução
    elif token == fim_instrucao:
        print(f"{token} -> Fim de instrução")

    # Caso não se encaixe em nenhuma categoria
    else:
        print(f"{token} -> Token desconhecido")