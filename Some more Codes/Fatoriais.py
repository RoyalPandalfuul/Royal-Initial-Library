# O Programa vai ler um numero natural e inteiro na entrada e imprimir um numero fatorial comum na saida.
num1 = int(input("Digite o Valor de n!: "))
NFatorial = num1

if num1 == 0 or num1 == 1:

    print("1")

else:

    while num1 != 1:
        NFatorial = NFatorial * (num1 - 1)
        num1 = num1 - 1

    
    print(NFatorial)