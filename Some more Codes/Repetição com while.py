print("O programa vai ler uma sequencia de numeros e dizer se há ou não numeros iguais adjacentes nela.")

sequencia = int(input("Digite um número inteiro: "))
sequenciaStr = str(sequencia)
UltimoNumero = 0
NumeroAtual = 0
QuantidadeDeDigitos = len(sequenciaStr)
repetição = 0
DeuCerto = False
if QuantidadeDeDigitos > 1 :
    while repetição != QuantidadeDeDigitos :
        NumeroAtual = (sequencia % 10)
        sequencia = (sequencia // 10)
        UltimoNumero = (sequencia % 10)
        repetição = repetição + 1
        if UltimoNumero == NumeroAtual :
            DeuCerto = True
else:
    print("não")

if DeuCerto == True :
    print("sim")
else:
    print("não")