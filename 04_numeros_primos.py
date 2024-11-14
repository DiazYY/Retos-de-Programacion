# Escribe un programa que se encargue de comprobar si un número es o no primo.

def numeroprimo(num):
    if num < 2:
        return False

    for divisor in range(2,num):
        if num % divisor == 0:
            return False
    return True    

# Hecho esto, imprime los números primos entre 1 y 100.

for numero in range(101):
    if numeroprimo(numero):
        print(numero)
 
