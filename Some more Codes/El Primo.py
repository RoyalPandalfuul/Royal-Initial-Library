print("O programa verifica se um número é primo ou não :) ")

num = int(input("Digite um número inteiro: "))

primo2 = num % 2 == 0
primo3 = num % 3 == 0
primo5 = num % 5 == 0
primo7 = num % 7 == 0

primeirosPrimos = (num == 2) or (num == 3) or (num == 5) or (num == 7)

if primeirosPrimos :

    print("primo")

else:
    if primo2 or primo3 or primo5 or primo7 or num == 1:

        print("não primo")

    else:

        print("primo")