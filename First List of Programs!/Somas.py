digitos = int(input("Digite a quantitade de digitos a ser somados: "))

soma = 0

valor = 0

rodadas = 0

while rodadas != digitos : 

    valor = int(input("Digite o valor a ser somado: "))

    soma = soma + valor 

    rodadas = rodadas + 1

print("O resultado da soma é: ",soma) 