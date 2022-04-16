from tkinter import TRUE
from trace import Trace


decrescente = True

anterior = int(input("Digite o primeiro numero da sequencia E caso queira terminar digite o numero zero: "))

valor = 1

while valor != 0 and decrescente :
    
    valor = int(input("Digite o seguinte numero da sequencia: "))
    
    if valor > anterior :

        decrescente = False
        
        anterior = valor

if decrescente :

    print("Parabens a sua sequencia está em ordem decrescente! :)")

else:

    print("Oh não! A sua sequencia não está em ordem decrescente! :(")