# Crea un programa que invierta el orden de una cadena de texto
# sin usar funciones propias del lenguaje que lo hagan de forma automática.
# - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

def invertir_cadena():
    word = input("ingresa la palabra que deseas invertir: ")
    print(word[::-1])

invertir_cadena()