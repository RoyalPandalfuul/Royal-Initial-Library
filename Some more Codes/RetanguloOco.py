# Este programa vai ler duas entradas e imprimir um objeto oco na saida! 

Largura = int(input("Digite o valor da largura!: "))
Altura = int(input("Agora digite o valor da altura!: "))

linha_cheia = '#' * Largura
linha_oca = '#' + (' ' * (Largura - 2) + '#')
print(linha_cheia)
i = 2
if Altura > 1:
  while i < Altura:
    print(linha_oca)
    i+= 1
  print(linha_cheia)