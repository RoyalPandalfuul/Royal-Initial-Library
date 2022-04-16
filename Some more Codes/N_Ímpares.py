print("O programa imprime uma quantidade de números ímpares, a quantidade vai na entrada de dados.")

num = int(input("Digite um número inteiro: "))
impressões = 0
QuantidadeDeDigitos = 0
num2 = 0

while impressões != num:
    if num2 % 2 != 0:
        print(num2)
        impressões = impressões + 1
    num2 = num2 + 1
