def usuario_escolhe_jogada(n,m):
    print("Usuario jogando")
    JogadaUsuario = int(input("Quantas peças? "))
    while JogadaUsuario > m :
        print("Jogada invalida!")
        JogadaUsuario = int(input("Quantas peças? "))
    n = (n - JogadaUsuario)
    return JogadaUsuario

def computador_escolhe_jogada(n,m):
    print("Computador Joga")
    if n <= m :
        return n - n #Tira o resto do tabuleiro
    else:
        if n % (m+1) == 0 : #Caso N seja multiplo 
            return n % (m+1) #Joga multiplos
        else:
            return m # não é multiplo, retira o máximo de peças

def partida():
    print("")
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    PcJoga = True
    if n % (m+1) == 0 :
        PcJoga = False
        print("Voce começa!")
    else:
        PcJoga = True
        print("Computador começa!")
    JogadaPessoa = n
    JogadaPc = n
    while n > 0 :
        if PcJoga == True :
            JogadaPc = computador_escolhe_jogada(JogadaPessoa,m)
            n = JogadaPessoa
            PcJoga = False
            if n == 1:
                print("O computador tirou uma peça.")
            else:
                print(f"O computador tirou {JogadaPc} peças.")
        else:
            JogadaPessoa = usuario_escolhe_jogada(JogadaPc,m)
            n = JogadaPc
            PcJoga = True
            if n == 1:
                print("O usuario tirou uma peça.")
            else:
                print(f"o usuario tirou {JogadaPessoa} peças.")
    if n <= 0 and PcJoga == False : # Caso o computador vença
        print("Fim do jogo! O computador ganhou!")
    else:
        print("Fim do jogo!")


def campeonato():
    partida()
    partida()
    partida()

partida()