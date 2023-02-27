#Cuando enviamos valores a la función.

def saludamos (nombre):
    return f"Hola, {nombre} desde la función saludar"

saludo = saludamos("Jorge Alexander tienes 47 años,")
print(saludo)

#Otro ejemplo:
print ("======================Otro ejemplo=============================")

def sumar (a, b):
    return a + b

suma = sumar (10, 90)
print("La suma es:", suma)

#Otro ejemplo:
print ("======================Otro ejemplo=============================")

def restar (a, b):
    return a - b

resta = restar (10, 90)
print("La resta es:", resta)

#Otro ejemplo:
print ("======================Otro ejemplo=============================")

def multiplicar (a, b):
    return a * b

multiplica = multiplicar (10, 90)
print("La multiplicación es:", multiplica)

#Otro ejemplo:
print ("======================Otro ejemplo=============================")

def dividir (a, b):
    return a / b

divide = dividir (900, 90)
print("La división es:", divide)


#Otro ejemplo:
print ("======================Otro ejemplo con valor none ============================")

def restar (a=None, b=None):
    if a == None or b == None: 
        print("Error: Debes enviar dos nñumeros a la función")
        return
    return a - b

resta = restar()
print("La resta es:", resta)
















