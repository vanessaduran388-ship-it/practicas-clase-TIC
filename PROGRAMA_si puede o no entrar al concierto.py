#programa para saber si si puedes entrar o no al concierto
#solicitar datos
edad=int(input("ingrese su edad "))
permiso=input("ingresa si tienes o no tienes permiso ")
if edad>=18 or permiso=="si":
    print("puedes entrar al concierto")
else:
    print("no puedes entrar al concierto")
#solicita un dato mas
acompañado=input("¿vas acompañado? ")
if edad>=18 or permiso=="si":
    print("puedes entrar al concierto")
elif edad>=18 or acompañado=="si":
    print("puedes entrar al concierto")
else:
    print("no puedes entrar")
