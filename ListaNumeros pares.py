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
i=0
while i<10:
    num=int(input("ingresa un numero: "))
    numPares.append(num)
    i=i+1
print("numeros pares: ")
for num in numPares:
    if num %2==0:
        print(num)
