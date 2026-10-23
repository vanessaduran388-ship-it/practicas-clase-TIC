#programa para calcular areas
#Area cuadrado;lado x lado
lado=float(input("ingresa lado"))
areaCuadrado=lado*lado 
print("El area es", areaCuadrado)
print(f"El area es {areaCuadrado}")
#Area de un triangulo (base x altura)/2
base=float(input("ingresa la base"))
altura=input("ingresa tu altura")
areaTriangulo= (base*altura)/2
print("el area es", areaTriangulo)
#Area de un trapecio (baseMayor+baseMenor)x altura /2
baseMayor=float(input("ingresa la base mayor"))
baseMenor=float(input("ingresa la baseMenor"))
altura=input("ingresa la altura")
areaTrapecio=((baseMayor+baseMenor)*altura)/2
print("el area es", areaTrapecio)
##extra-----area del circulo y pentagono
#Area del circulo area= pi x radio2
PI=(3.1416)
radio=float(input("ingresa el radio del circulo"))
areaCirculo=PI*(radio*radio)
print("el area es", areaCirculo)
#area del pentagono area=perimetro x apotema /2
perimetro=float(input("ingresa el perimetro"))
apotema=float(input("ingresa el apotema"))
areaPentajono=(perimetro*apotema)/2
print("el area es", areaPentajono)
