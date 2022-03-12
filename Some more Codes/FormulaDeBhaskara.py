import math

ValorDeA = float(input("Insira o valor de A: "))

ValorDeB = float(input("Insira o valor de B: "))

ValorDeC = float(input("Insira o valor de C: "))

delta = ValorDeB ** 2 - 4 * ValorDeA * ValorDeC

if delta == 0:
    raiz1 = (-ValorDeB + math.sqrt(delta)) / (2 * ValorDeA)
    print("A unica raiz é: ",raiz1)
else:
        if delta < 0:
            print("Essa equação não tem raizes reais.")
        else:
                raiz1 = (-ValorDeB + math.sqrt(delta)) / (2 * ValorDeA)

                raiz2 = (-ValorDeB - math.sqrt(delta)) / (2 * ValorDeA)
                
                print("A primeira raiz é: ",raiz1)
                print("A segunda raiz é: ",raiz2)