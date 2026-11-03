nombre="melanie"
frase="las aguilas vuelan alto"
print(nombre)
print(frase)
#mostrar el nombre en mayus
print(nombre.upper())
print(frase.upper())
#mostrar en minusculas
print(frase.lower())
#obtener un caracter en una posicion
letra=frase[4]
print(letra)
frase2="las-aguilas-vuelan-alto"
print(frase2.split("-"))
nombreC="melanie vanessa duran lopez"
print(nombreC.split(" "))
#dos primeras letras del nombre
letras1=nombreC[0:2]
print(letras1)
#remplazarla en la cadena
nuevaFrase=frase.replace("vuelan alto","cazan conejos")
print(nuevaFrase)
#numero de caracteres de la cadena: largo
largoCadena=len(nuevaFrase)
print(largoCadena)
