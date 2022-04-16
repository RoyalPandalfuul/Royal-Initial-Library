# Exercisio pensando na aula de indicadores de passagem.

cpf = int(input("Digite o numero do seu cpf(não de vdd ok) e Digite 0 quando quiser terminar: "))

AcheiMeuCpf = False

QualquerCpf = 1

while AcheiMeuCpf == False and QualquerCpf != 0 :

    QualquerCpf = int(input("Digite qualquer cpf para ver se foi vazado:"))

    if QualquerCpf == cpf :

        AcheiMeuCpf = True

if AcheiMeuCpf == True:

    print("Seu cpf foi vazado :( ")

else:

    print("Teu cpf n foi vazado n, rlx :) ")