while True:
    try:
        altura = int(input("Qual a altura do triângulo? (máx 20): "))
        
        if 1 <= altura <= 20:    #Se o número estiver entre 1 e 20, já pula para o loop para mostrar o triângulo
            break
        else:
            print("Digite um número entre 1 e 20.")     #Reforça que precisa digitar um número entre 1 e 20
    
    except ValueError:
        print("Digite apenas números inteiros.")   #except para nao quebrar caso a pessoa digite algo diferente de um número

for i in range(1, altura + 1):     #loop para mostrar o triangulo
    print("*" * i)