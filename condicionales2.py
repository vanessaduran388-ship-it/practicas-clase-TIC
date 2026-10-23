#programa que me indica como me fue en las calificaciones
calif=float(input("dame tu calif"))
if calif==10:
    print("excelente")
elif calif==9:
    print("muy bien")
elif calif==8:
    print("bien")
elif calif==7:
    print("puedes mejorar")
elif calif==6:
    print("ay mijooo")
else:
    print("chanclazooo")

#solicitar una temperatura
temp=float(input("dame tu temp"))
if temp==40:
    print("hace mucho calor") 
elif temp==30 and temp<40:
    print("esta templadito")
elif temp==20 and temp<30:
    print("esta fresco")
elif temp==10:
    print("hace frio")
else:
    print("no valido")

#solicitar sexo
#solicitar edad 
sexo=input("ingresa tu sexo ")
edad=int(input("ingresa tu edad "))
if sexo=="hombre" and edad>=18:
    print("puedes sacar cartilla militar")
else:
    print("no puedes")

 