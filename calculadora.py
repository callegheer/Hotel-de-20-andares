def calculadora(n1, n2, operacao):
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
    
resultado = calculadora(2, 9, 2)
print(resultado)