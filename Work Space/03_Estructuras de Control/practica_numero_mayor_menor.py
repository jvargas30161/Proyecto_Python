# ENUNCIADO : Ingrese 6 números en una lista y obtenga el número mayor y menor ingresado.
# ANÁLISIS  : Para la solución de este problema, se requiere que el usuario ingrese 6 números,
# luego el sistema devuelva el número mayo y menor.
# ENTRADA
#           · 6 Números (n).
# SALIDA
#           · Mayor (mayor).
#           · Menor (menor)

# Ingresar Datos / Lista
num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
num3 = int(input('Número 3: '))
num4 = int(input('Número 4: '))
num5 = int(input('Número 5: '))
num6 = int(input('Número 6: '))

# Usando la función append()
numeros = []
numeros.append(num1)
numeros.append(num2)
numeros.append(num3)
numeros.append(num4)
numeros.append(num5)
numeros.append(num6)

# Solución
minimo = maximo = numeros[0]

for numeros in numeros:
    if numeros < minimo:
        minimo = numeros
    elif numeros > maximo:
        maximo = numeros

    # Mostrar Datos
print("El mínimo es " + str(minimo))
print("El máximo es " + str(maximo))



### Otra respuesta:
print("============================otra respuesta=====================")

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
num4 = int(input("Ingrese el cuarto numero: "))
num5 = int(input("Ingrese el quinto numero: "))
num6 = int(input("Ingrese el sexto y ultimo numero: "))

numeros = [num1, num2, num3, num4, num5, num6]

for i in range(len([numeros])):
    Mayor = 0
    Menor = 0
    if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5 and num1 > num6:
        Mayor = num1
        print("El primero es el mayor:", Mayor)
    elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5 and num2 > num6:
        Mayor = num2
        print("El segundo es el mayor:", Mayor)
    elif num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5 and num3 > num6:
        Mayor = num3
        print("El tercero es el mayor:", Mayor)
    elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5 and num4 >  num6:
        Mayor = num4
        print("El cuarto es el mayor:", Mayor)
    elif num5 > num1 and num5 > num2 and num5 > num3 and num5 > num4 and num5 >num6:
        Mayor = num5
        print("El quinto es el mayor:", Mayor)
    elif num6 > num1 and num6 > num2 and num6 > num3 and num6 > num4 and num6 > num5:
        print("El sexto es el mayor:", Mayor)
        Mayor = num6
for i in range(len([numeros])):
    if num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5 and num1 < num6:
        Menor = num1
        print(f"El primero es el menor: {Menor}")
    elif num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5 and num2 < num6:
        Menor = num2
        print(f"El segundo es  el menor: {Menor}")
    elif num3 < num1 and num3 < num2 and num3 < num4 and num3 < num5 and num3 < num6:
        Menor = num3
        print(f"El tercero es el menor: {Menor}")
    elif num4 < num1 and num4 < num2 and num4 < num3 and num4 < num5 and num4 < num6:
        Menor = num4
        print(f"El cuarto es el menor: {Menor}")
    elif num5 < num1 and num5 < num2 and num5 < num3 and num5 < num4 and num5 < num6:
        Menor = num5
        print(f"El quinto es el menor: {Menor}")
    else:
        Menor = num6
        print(f"El sexto es el menor: {Menor}")


print("===================Otra respuesta============================")

# Ingresar Datos / Lista
num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
num3 = int(input('Número 3: '))
num4 = int(input('Número 4: '))
num5 = int(input('Número 5: '))
num6 = int(input('Número 6: '))

# Usando la función append()
num = []
numeros.append(num1)
numeros.append(num2)
numeros.append(num3)
numeros.append(num4)
numeros.append(num5)
numeros.append(num6)

minimo = maximo = numeros[0]
for numeros in numeros:
    # if minimo < numeros :
    #   minimo = numeros
    #elif maximo > numeros:
    #  maximo= numeros

    if numeros < minimo:
        minimo = numeros
    elif numeros > maximo:
        maximo = numeros

    # Mostrar Datos
print("El número mínimo es " ,minimo)
print("El número máximo es ", maximo)