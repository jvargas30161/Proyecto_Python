# Variables | Ingresar Datos.
numero1 = int(input('Número 1: '))
numero2 = int(input('Número 2: '))
numero3 = int(input('Número 3: '))

# Solución

# Hallar el número mayor
if numero1 > numero2 and numero1 > numero3:
    mayor = numero1
else:
    if numero2 > numero1 and numero2 > numero3:
        mayor = numero2
    else:
        mayor = numero3

# Hallar el número menor
if numero1 < numero2 and numero1 < numero3:
    menor = numero1
else:
    if numero2 < numero1 and numero2 < numero3:
        menor = numero2
    else:
        menor = numero3

# Hallar el número intermedio
intermedio = (numero1 + numero2 + numero3) - (mayor - menor)

# Mostrar Datos
print(f'Mayor: {mayor}')
print(f'Intermedio: {intermedio}')
print(f'Menor: {menor}')


print("---------otro ejemplo -----------------")

n1= input ("entre numero 1: ")
n2= input ("entre numero 2")
n3= input ("entre numero 3")
sequencia = [n1,n2,n3]
numeros_ordenados = sorted(sequencia)
print (sequencia)
print (numeros_ordenados)


print("---------otro ejemplo -----------------")
r=0
lista = []
for r in range (r,3):
    numero = int(input('Ingrese un numero: '))
    lista.append(numero)
    lista.sort()

print(lista)


print("---------otro ejemplo -----------------")
n1=int(input('Ingrese el 1er.Nro:)'))
n2=int(input('Ingrese el 2do.Nro:)'))
n3=int(input('Ingrese el 3do.Nro:)'))

if n1>n2 and n1>n3:
    mayor=n1
else:
    if n2>n1 and n2>n3:
        mayor=n2
    else:
        mayor=n3
if n1<n2 and n1<n3:
    menor=n1
else:
    if n2<n1 and n2<n3:
        menor=n2
    else:
        menor=n3


intermedio=(n1+n2+n3)-(mayor+menor)

print('-'*50)
print (menor, intermedio, mayor)
print('-'*50)
print ('MENOR', menor)
print ('INTERMEDIO', intermedio)
print ('MAYOR', mayor)
print('-'*50)