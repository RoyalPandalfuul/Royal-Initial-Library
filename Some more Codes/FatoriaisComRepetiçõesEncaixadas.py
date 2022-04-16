#Exercisio para treinar a aplicação de repetições encaixadas, while dentro de while
print("Este programa calcula o fatorial de um número na entrada e o imprime na saida! ultilizando repetições encaixadas :)")
print("")
def fatorial(a):
    NFatorial = a
    if a == 0 or a == 1:
        return 1
    else:
        while a != 1:
            NFatorial = NFatorial * (a - 1)
            a = a - 1
        return NFatorial

while True : 
    num = int(input("Digite um número para saber o fatorial dele! : "))
    NFatorial = fatorial(num)
    print(f"O Fatorial de {num} é {NFatorial}")
