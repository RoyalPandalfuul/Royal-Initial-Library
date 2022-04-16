# Este programa recebe un número maior que 2 na entrada e conta os primos de 2 até ele :)

def primaridade(a): 
    primo2 = a % 2 == 0
    primo3 = a % 3 == 0
    primo5 = a % 5 == 0
    primo7 = a % 7 == 0
    primeirosPrimos = (a == 2) or (a == 3) or (a == 5) or (a == 7)

    if primeirosPrimos :
        return True
    else:
        if primo2 or primo3 or primo5 or primo7 or a == 1:
            return False
        else:
            return True

def n_primos(x):
    TotalPrimos = 1
    Repetição = x
    if x == 2:
        return 1
    while Repetição > 2 :
        if primaridade(x) == True :
            TotalPrimos = TotalPrimos + 1
        Repetição = Repetição - 1
        x = x - 1
    return TotalPrimos
