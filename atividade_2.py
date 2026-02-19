# Loop para garantir que o usuário digite um valor válido
while True:
    try:
        # Pede o tamanho do quadrado
        tamanho = int(input("Tamanho do quadrado (máx 20): "))
        
        # Verifica se está dentro do limite permitido
        if 1 <= tamanho <= 20:
            break  # Sai do loop se for válido
        else:
            print("Digite um número entre 1 e 20.")
    
    # Caso o usuário digite algo que não seja número
    except ValueError:
        print("Digite apenas números inteiros.")


# ===============================
# 1️⃣ Imprime o quadrado completo
# ===============================

print("\nQuadrado completo:\n")

# Para cada linha do quadrado
for i in range(tamanho):
    # Imprime uma linha com 'tamanho' estrelas
    print("*" * tamanho)


# =======================================
# 2️⃣ Imprime apenas a diagonal superior direita
# =======================================

print("\nDiagonal superior direita:\n")

# Percorre cada linha
for i in range(tamanho):
    
    # Percorre cada coluna da linha atual
    for j in range(tamanho):
        
        # Condição da diagonal superior direita:
        # coluna == tamanho - linha - 1
        # Isso faz a estrela aparecer do canto superior direito
        # até o canto inferior esquerdo
        if j == tamanho - i - 1:
            print("*", end="")  # Imprime estrela sem quebrar linha
        else:
            print(" ", end="")  # Imprime espaço
        
    # Quebra de linha ao final de cada linha
    print()