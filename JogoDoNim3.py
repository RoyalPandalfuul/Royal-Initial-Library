
def usuario_escolhe_jogada(n,m):
    JogadaDoUsuario = int(input("Digite o numero de peças a tirar: "))
    while (JogadaDoUsuario > m) or (JogadaDoUsuario <= 0) :
        print("Digite um número valido!")
        JogadaDoUsuario = int(input("Digite o numero de peças a tirar: "))
    if JogadaDoUsuario == 1:
        print("Você tirou uma peça.")
    else:
        print(f"Você tirou {JogadaDoUsuario} peças.")
    return JogadaDoUsuario

def computador_escolhe_jogada(n,m):
    if n % (m+1) != 0: #Casso seja multiplo
        print(f"Computador tirou {(n % (m+1))} peças")
        return (n % (m+1))
    else:
        print(f"Computador tirou {m} peças")
        return m
    

def partida():
    n = int(input("Digite o número de peças no tabuleiro: "))

    m = int(input("Digite o número máximo de peças a tirar: "))

    if n % (m+1) == 0 : 
        print("")
        print("Voce começa!")
        while n > 0 :
            n = n - usuario_escolhe_jogada(n,m)
            print(f"Agora restam {n} peças")
            if n > 0 :
                n = n - computador_escolhe_jogada(n,m)
                print(f"Agora restam {n} peças")
        print("Computador ganhou!")
    else:
        print("")
        print("Computador começa!")
        while n > 0 :
            n = n - computador_escolhe_jogada(n,m)
            print(f"Agora restam {n} peças")
            if n > 0 :
                n = n - usuario_escolhe_jogada(n,m)
                print(f"Agora restam {n} peças")
        print("Computador ganhou!")

def campeonato():
    print("")
    print("**** Rodada 1 ****")
    print("")
    partida()
    print("")
    print("**** Rodada 2 ****")
    print("")
    partida()
    print("")
    print("**** Rodada 3 ****")
    print("")
    partida()
    print("**** Final do campeonato! ****")
    print("")
    print("Placar: Você 0 X 3 Computador")

def main():
    print("")
    Entrada = int(input("Bem-vindo ao jogo do NIM! Escolha: \n 1 - para jogar uma partida isolada \n 2 - para jogar um campeonato 2"))
    if Entrada == 1:
        print("")
        print("Voce escolheu partida!")
        partida()
    else:
        print("")
        print("Voce escolheu um campeonato!")
        campeonato()

main()