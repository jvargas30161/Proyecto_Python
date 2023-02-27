## Podemos realizar operaciones con cadenas de caracteres

print("========== Metodo upper==========")
##Convertiremos de minuscula a mayuscula

print("Hola Mundo".upper())
print("Jorge Alexander Vargas Sanchez".upper())

print("========== Metodo lower==========")
##Convertiremos de mayuscula a minuscula

print("Hola Mundo".lower())
print("Jorge Alexander Vargas Sanchez".lower())


print("========== Metodo capilize==========")
##Convertiremos el primer caracter en mayuscula

print("Hola Mundo".capitalize())
print("Jorge Alexander Vargas Sanchez".capitalize())

print("========== Metodo title==========")
##Convertiremos en modo título

print("Hola Mundo".title())
print("JORGE Alexander Vargas Sanchez".title())


print("========== Metodo count==========")
##Contaremos los caracteres

print("Hola Mundo".count("o"))
print("JORGE Alexander Vargas Sanchez".count("A"))
print("JORGE Alexander Vargas Sanchez".count("a"))


print("================== Metodo Remplace====================")
## reemplazamos datos

palabra = "Python"
palabra = palabra.replace("P", "S")
print (palabra)

print("========== Metodo Remplace cuando hay espacios en blanco==========")
## reemplazamos datos espacios en blanco por no espacios

palabra = "J o r g e_A l e x a n d e r"
palabra = palabra.replace(" ", "")
print (palabra)

print("========== Metodo strip cuando hay espacios en blanco derecha e izquierda==========")
## reemplazamos datos espacios en blanco por no espacios

palabra = "   J o r g e  A l e x a n d e r      "
palabra = palabra.strip()
print (palabra)


print("========== Metodo strip cuando hay guiones derecha e izquierda==========")
## reemplazamos datos espacios en blanco por no espacios

palabra = "-----------J o r g e -  A l e x a n d e r -------------"
palabra = palabra.strip("-")
print (palabra)


print("========== Metodo split cuando queremos que caracteres se conviertan en lista==========")
## reemplazamos datos espacios en blanco por no espacios

palabra = "Jorge Alexander Vargas Sanchez"
palabra = palabra.split()
print (palabra)


print("========== Metodo split cuando queremos que caracteres se conviertan en lista==========")
## Podemos elegir que caracer se convertira en una lista

palabra = "Jorge,Alexander,Vargas,Sanchez"
palabra = palabra.split(",")
print (palabra)


print("========== Metodo islower para verificar si el dato es solo minuscula==========")
##
palabra = "jorge"
palabra = palabra.islower()
print (palabra)

print("========== Metodo islower para verificar si el dato es solo minuscula==========")
##
palabra = "Jorge"
palabra = palabra.islower()
print (palabra)


print("========== Metodo isupper para verificar si el dato es solo mayuscula==========")
##
palabra = "JorgE"
palabra = palabra.isupper()
print (palabra)


palabra = "JORGE"
palabra = palabra.isupper()
print (palabra)


print("========== Metodo istittle para verificar si el dato es título==========")
##

print("Hola Mundo Estamos Muy Bien".istitle())   ##True
print("Hola Mundo Estamos Muy bien".istitle())  ##False


print("========== Metodo isspace para verificar si ha puros espacios==========")
##

print("                              ".isspace())   ##True
print("Hola Mundo Estamos Muy bien".isspace())      ##False
print("             e                 ".isspace())   ##False












