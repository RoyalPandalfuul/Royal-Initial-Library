# O Programa vai ler números na entrada e aplicar a fórmula de coeficientes binomiais.

def fatorial(num):
    NumFatorial = num
    if num == 0:
        return 1
    else:
    
        if num < 0 :
            return 0
        else:
         while num != 1 :
                NumFatorial = NumFatorial * (num - 1)
                num = num - 1
                return NumFatorial

def testa_fatorial():
    if fatorial(1) == 1:
        print("Funciona para 1")
    else:
        print("Não funciona para 1")
    if fatorial(2) == 2:
        print("Funciona para 2")
    else:
        print("Não funciona para 2")
    if fatorial(5) == 120:
        print("Funciona para 5")
    else:
        print("Não funciona para 5")
    if fatorial(0) == 1:
        print("Funciona para 0")
    else:
        print("Não funciona para 0")    
    
def coeficiente(n, k):
    
    return  fatorial(n) /  (fatorial(k) * fatorial(n-k))

# Agora é só implementar oq deseja imprimir na linha de baixo e rodar o programa :)

print(fatorial(-15))
