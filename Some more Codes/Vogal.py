#Este programa le uma letra na entrada e imprime se é vogal ou não na saida.
Letra = input("Digite a letra a ser julgada: ")

def vogal(a):
    if a == "a" or a == "e" or a == "i" or a == "o" or a == "u" :
        return True
    else:
        return False

print(vogal(Letra))