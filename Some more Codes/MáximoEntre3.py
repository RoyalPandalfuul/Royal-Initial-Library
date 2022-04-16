#Este programa pega o valor máximo de 3 entradas em uma função e devolve o maior.

def maximo(a, b, c):
    if a > b and a > c:
        return a
    else:
        if b > a and b > c:
            return b
        else:
            if c > a and c > b:
                return c
            else:
                if a > b:
                    return a
                else:
                    if b > a:
                        return b
                    else:
                        if c > a:
                            return c
                        else:
                            if a > c:
                                return a
