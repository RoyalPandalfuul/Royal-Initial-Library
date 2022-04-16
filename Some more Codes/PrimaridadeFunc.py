print("O programa verifica se um número é primo ou não usando uma função e repetições encaixadas! ")

def primaridade(a): #Ultilizei o mesmo que em programas anteriores, mas agora como função
    primo2 = num % 2 == 0
    primo3 = num % 3 == 0
    primo5 = num % 5 == 0
    primo7 = num % 7 == 0
    primeirosPrimos = (num == 2) or (num == 3) or (num == 5) or (num == 7)

    if primeirosPrimos :
        return True
    else:
        if primo2 or primo3 or primo5 or primo7 or num == 1:
            return False
        else:
            return True

num = int(input("Digite um número inteiro a ser testado: "))
while num > 0 :
    if primaridade(num) == True :
        print("Este número é primo!")
    else:
        print("Este número não é primo")
    num = int(input("Digite um número inteiro a ser testado: "))
    
