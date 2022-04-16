#Este programa tem uma função que devolve fizz se for divisível por 3, buzz se for divisível por 5 e fizzbuzz se for divisível por 3 E 5.

def fizzbuzz(num):
    if (num % 3 == 0 and num % 5 == 0) :
        return "FizzBuzz"
    else:
        if (num % 3 == 0):
            return "Fizz"
        else:
            if (num % 5 == 0):
                return "Buzz"
            else:
                return num

