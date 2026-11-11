#numeros pares
numeros=[]
i=0
while i<10:
    num=int(input("ingresa un numero"))
    numeros.append(num)
    i=i+1
print("numeros pares: ")
for num in numeros:
    if num % 2==0:
        print(num)

#extra
#has una lista donde agregue los que son pares
numPares=[]
for num in numeros:
    if num % 2==0:
        numPares.append(num)
    print("numeros pares")
for p in numPares:
    print(p)
