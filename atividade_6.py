# ==============================
# Simulação de fechadura eletrônica
# Senha correta: 1-2-3
# ==============================

senha = input("Digite a senha (formato 1-2-3): ")

estado = 0  # Estado inicial

# Remove os delimitadores "-"
senha_limpa = senha.replace("-", "")

# Percorre cada caractere da senha
for caractere in senha_limpa:

    match estado:

        case 0:
            # Se estiver no estado 0 e digitar 1 → vai para estado 1
            if caractere == "1":
                estado = 1
            else:
                estado = 0

        case 1:
            # Se estiver no estado 1 e digitar 2 → vai para estado 2
            if caractere == "2":
                estado = 2
            else:
                estado = 0

        case 2:
            # Se estiver no estado 2 e digitar 3 → vai para estado 3
            if caractere == "3":
                estado = 3
            else:
                estado = 0

        case 3:
            # Se já chegou no estado final, permanece
            estado = 3


# ==============================
# Verificação final
# ==============================

if estado == 3:
    print("Acesso concedido!")
else:
    print("Acesso negado!")