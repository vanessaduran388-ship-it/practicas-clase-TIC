#busqueda
nombres=["angel","karla","luis","mateo","maria","luis","karla"]
print(f"los nombres que se tienen son:{nombres}")
nombreBuscar=input("¿que nombre deseas buscar?: ")
encontrado=False
contador=0
i=0
while i<len(nombres):
    if nombres[i]==nombreBuscar:
        encontrado=True
        contador=contador+1
        print("encontrado en la posicion:",i)
    i=i+1
if encontrado==True:
    print("nombre encontrado")
    print("aparece",contador,"veces")
else:
    print("nombre no encontrado")

#extra
if contador>1:
    while nombreBuscar in nombres:
        nombres.remove(nombreBuscar)
        print(f"se elimino el nombre que mas se repite")
print(nombres)