#numeros y multiplicacion
numeros=[]
resultados=[]
i=0
while i<5:
    num=int(input("ingresa un numero: "))
    numeros.append(num)
    i=i+1
multiplicador=int(input("¿por cuanto quieres multiplicar?: "))
for num in numeros:
    resultado=num*multiplicador
    resultados.append(resultado)
print("numeros originales;", numeros)
print("resultados:", resultados)

#extra
print(f"los numeros de la lista son:¨{numeros}")
numBuscar=input("¿que numero quieres buscar?: ")
encontrado=False
contador=0
i=0
while i<len(numeros):
    if numeros[i]==numBuscar:
        encontrado=True
        contador=contador+1
        i=i+1
        if encontrado==True:
            print("numero encontrado")
        else:
            print("numero no encontrado")