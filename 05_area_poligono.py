# Crea una única función (importante que sólo sea una) que sea capaz
# de calcular y retornar el área de un polígono.
# - La función recibirá por parámetro sólo UN polígono a la vez.
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.

figura = input('escriba el nombre del poligono, al cual desea calcular el area, "cuadrado", "triangulo" o "rectangulo": ')

def calcular_area(poligono):
    if poligono == "triangulo":
        base = float(input('Ingrese la base: '))
        altura = float(input("Ingrese la altura: "))
        print(f"El area del {poligono} es {(base * altura) / 2}")
    elif poligono == "cuadrado":
        lado = float(input('Ingrese la longitu de uno de los lados: '))
        print(f"El area del {poligono} es {lado ** 2}")
    elif poligono == "rectangulo":
        base = float(input('Ingrese la longitu de uno de los lados: '))
        altura = float(input("Ingrese la altura: "))
        print(f"El area del {poligono} es {base * altura}")
    else:
        print("no se que figura es")

calcular_area(figura)