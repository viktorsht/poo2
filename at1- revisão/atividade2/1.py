lado1 = float(input("Lado 1: "))
lado2 = float(input("Lado 2: "))
lado3 = float(input("Lado 3: "))

triangulo = False

if (lado1 + lado2 > lado3) | (lado2 + lado3 > lado1) | (lado3 + lado1 > lado2):
    triangulo = True

if(triangulo == True):
    if lado1 == lado2 and lado1 == lado3:
        t = "Equilátero"
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        t = "Isósceles"
    else:
        t = "Escaleno"

if(triangulo == True):
    print("triangulo " + t)
else:
    print("Impossível ser um triangulo")
