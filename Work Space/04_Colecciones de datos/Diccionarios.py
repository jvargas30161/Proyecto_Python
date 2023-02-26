# Aprenderemos a definir un diccionario 

print ("*****************Primer Ejemplo*********************")
numeros = {}
print(numeros)


print ("*****************Segundo Ejemplo*********************")
numeros = { "uno":1, "dos":2, "tres":3, "cuatro":4, "ocho":100}
print(numeros)


print ("*************Tercer Ejemplo accederemos a sus elementos usando la clave*******")
print (numeros["cuatro"])
print (numeros["uno"])
print (numeros["ocho"])


print ("*************Cuarto Ejemplo Modificaremos o agregamos un nuevo elemento ******")
numeros["quince"] = 15
print(numeros)


print ("*************Buscar utilizando metodos de diccionario  ******")
print (numeros.get("dos", "No se encontró el elemento"))


print ("*************Buscar todas las claves del diccionario  ******")
print (numeros.keys())


print ("*************Buscar todos los valores del diccionario  ******")
print (numeros.values())


print ("*************Buscar Lista con clave  valor  ******")
print (numeros.items())

print ("*************Eliminar un valor de una lista  ******")
print (numeros.pop("noventa", "No se encontró el elemento "))


print ("*************Eliminar datos del diccionario  ******")
print (numeros.clear())
print (numeros)
print (type(numeros))


print ("*************iteraciones de las claves  ******")
numeros = { "uno":1, "dos":2, "tres":3, "cuatro":4, "ocho":100}
for numero in numeros:
    print(numero)

print ("*************iteraciones de los números  ******")
numeros = { "uno":1, "dos":2, "tres":3, "cuatro":4, "ocho":8}
for numero in numeros.values():
    print(numero)


print ("*************iteraciones clave  valor  ******")
for clave, valor in numeros.items():
    print(clave, valor)



    
