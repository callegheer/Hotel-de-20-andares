def calculadora (n1, n2, operacao):
    if (operacao == 1):
        return n1 + n2
    elif (operacao == 2):
        return n1 - n2
    elif (operacao == 3):
        return n1 * n2
    elif (operacao == 4):
        return n1 / n2
    else:
        return 0
    
executar = True
    
while (executar == True):
    print("Olá seja bem vindo! Escolha a operação que deseja realizar:")
    print("1. Soma", "2. Subtração", "3. Multiplicação", "4. Divisão", "0. Sair")
    operacao = int(input("Digite o numero para inciar a operação:"))
    if(operacao < 0) or (operacao > 4):
        print("Opção inválida, não existe!")
    elif(operacao == 0):
        executar = False
    else:
        print("Digite o primeiro número do cálculo:")
        n1 = int(input())
        print("Digite o segundo número do cálculo:")
        n2 = int(input())
        resultado = calculadora(n1, n2, operacao)
        print("Resultado:", resultado)