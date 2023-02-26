#Mientras que esta condicion devuelve verdadero, esta ejecución se puede ejecutar infinitamente.

#while True:
#    print("Bucle Infinito")

#Otro ejemplo de bucle.
c = 0
while c < 10:
    c+=1
    print("Valor de c", c )

n= int(input("Ingrese un número: "))

suma = 0
menores_n = 0

while menores_n < n:
    suma += menores_n
    menores_n += 1

print("La suma es: ", suma )





