#Este programa imprime um objeto com "#" de acordo com as medidas da entrada.

from re import X


y=int(input("Digite o tamaho da largura do objeto!: "))
x=int(input("Agora digite o tamanho da altura do objeto!: "))
alturaX = 0
larguraY = 0
while x != alturaX :
    while y != larguraY :
        print("#", end="")
        larguraY = larguraY + 1
    print("")
    alturaX = alturaX + 1
    larguraY = 0
