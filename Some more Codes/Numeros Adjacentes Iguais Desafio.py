print("O programa vai ler uma sequencia de numeros e dizer se há ou não numeros iguais adjacentes nela.")

sequencia1 = int(input("Digite a sequencia de numeros a ser analisada: "))
sequenciaStr = str(sequencia1)

UltimoNumero = 2
NumeroAtual = 1
sequenciaAcabou = False
QuantidadeDeDigitos = len(sequenciaStr)
repetição = 0

while UltimoNumero != NumeroAtual or sequenciaAcabou == False :
    NumeroAtual = (sequencia1 % 10)
    UltimoNumero = (sequencia1 % 100)
    sequencia1 = (sequencia1 // 10)
    repetição = repetição + 1
    
    if repetição == QuantidadeDeDigitos :
        sequenciaAcabou = True

if UltimoNumero == NumeroAtual :
    print("Essa sequencia tem numeros adjacentes iguais! :) ")

else:
    print("essa sequencia não tem numero adjacentes iguais! :( ")