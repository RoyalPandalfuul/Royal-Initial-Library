print("Este programa vai ler cada digito da sequencia que o usuario digitar, e soma-los em um resultado final.")

sequencia = int(input("Digite um número inteiro: "))
repetição = 0
soma = 0
novoNum = 0
strSequencia = str(sequencia)
QuantidadeDeDigitos = len(strSequencia)

while repetição != QuantidadeDeDigitos:
    novoNum = (sequencia % 10)
    soma = soma + novoNum
    sequencia = int(sequencia // 10)
    repetição = repetição + 1

print(soma)