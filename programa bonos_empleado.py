#programa que me indica un programa de bonos de los empleados
#solicitar datos del empleado
nombre=input("ingresa nombre del empleado")
pagoHora=float(input("ingresa tu pago por hora"))
horasMes=float(input("ingresa las horas trabajadas al mes"))
#calcular sueldo 
sueldo=pagoHora*horasMes
if sueldo>=100  and sueldo<300:
    print("bono $500")
    sueldoTotal=sueldo+500
    print("tu sueldo total es ", sueldoTotal)
elif sueldo>=800 and sueldo<1500:
    print("bono $1700")
    sueldoTotal=sueldo+500
    print("tu sueldo total es",sueldoTotal)
elif sueldo>=1500 and sueldo<3000:
    print("bono 3500")
    sueldoTotal=sueldo+500
    print("tu sueldo total es",sueldoTotal)
elif sueldo>=3000 and sueldo<8000:
    print("bono 8500")
    sueldoTotal=sueldo+500
    print("tu sueldo total es",sueldoTotal)
elif sueldo>=8000:
    print("bono 10000")
    sueldoTotal=sueldo+500
    print("tu sueldo total es",sueldoTotal)
else:
    print("no valido")
