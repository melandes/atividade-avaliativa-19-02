# ==============================
# Entrada dos conjuntos
# ==============================

# O usuário digita números separados por espaço
entrada_A = input("Digite os elementos do conjunto A separados por espaço: ")
entrada_B = input("Digite os elementos do conjunto B separados por espaço: ")

# split() divide a string em uma lista
# map(int, ...) converte cada elemento para inteiro
# set(...) remove elementos duplicados automaticamente

A = set(map(int, entrada_A.split()))
B = set(map(int, entrada_B.split()))

# ==============================
# Operações
# ==============================

uniao = A | B           # União
intersecao = A & B      # Interseção

# ==============================
# Saída
# ==============================

print("A =", A)
print("B =", B)
print("União:", uniao)
print("Interseção:", intersecao)