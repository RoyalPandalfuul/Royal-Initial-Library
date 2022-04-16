# #Este é o jogo do NIM! o usuario vai jogar ele com o código! o objetivo é remover a ultima peça do tabuleiro, quem a remover ganha!

# # use a função (??) para começar

# def multiplo(k):


# def computador_escolhe_jogada(n, m):
#     NumeroDePeças = n
#     MaximoATirar = m
#     Tirada = multiplo(n)
#     #A Função multiplo, que define a estratégia vencedora vai aqui.

# def usuario_escolhe_jogada(n, m):
#         NumeroDePeças = n
#         MaximoATirar = m
#         Tirou = False
#         while Tirou == False:
            
#             valorTirado = int(input("Quantas peças você vai tirar? "))
            
#             if (valorTirado <= MaximoATirar) and (valorTirado > 0) and valorTirado == 1:
#                 Tirou = True
#                 print("Você tirou uma peça.")

#             elif (valorTirado <= MaximoATirar) and (valorTirado > 0):
#                 Tirou = True
#                 print("Você tirou",valorTirado,"peças.")

#             else:
#                 Tirou = False
#                 print("Oops! Jogada inválida! Tente de novo.")

#         if Tirou == True :
#             print("Agora restam",(NumeroDePeças - valorTirado),"peças no tabuleiro.")
#         elif Tirou == True and (NumeroDePeças - valorTirado == 1):
#             print("Agora resta apenas 1 peça no tabuleiro.")


# usuario_escolhe_jogada(10, 5)

def computador_escolhe_jogada(n,m):
    JogadaDoPc = 1
    if JogadaDoPc % (m+1) == 0 :
        

def usuario_escolhe_jogada(n,m):
    Jogada = n - int(input("Quantas peças? "))
    print(JogadaDoUsuario)

def partida():
    print("")
    Jogada = 

    n = int(input("Digite a quantidade de peças: "))

    m = int(input("Quantidade maxima de peças a retirar: "))

    if n %  (m+1) == 0 : 
        print("Você começa!")
        usuario_escolhe_jogada(n,m)
    else:
        print("Computador começa!")
        computador_escolhe_jogada(n,m)
        

partida()