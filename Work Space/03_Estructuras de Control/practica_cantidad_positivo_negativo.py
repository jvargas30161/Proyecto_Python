valor1 = int(input('Número inicial: '))
valor2 = int(input('Número final: '))
valor2 += 1
cantidadPositivos = 0
cantidadNegativos = 0

# Solución
for numero in range(valor1, valor2):
    if numero % 2 == 0 :
        cantidadPositivos += 1
    else:
        cantidadNegativos += 1


# Mostrar Datos
print('Cantidad POSITIVOS: ', cantidadPositivos)
print('Cantidad NEGATIVOS: ', cantidadNegativos)



print ("----------------------otro ejemplo---------------------------")

print('   ---- TAREA 26 ----')
r1 = int(input('Ingrese Número inicio: '))
r2 = int(input('Ingrese Número final: '))
print('*'*25)

# Solución
positivos = 0
negativos = 0

for i in range(r1,r2):
    if i >= 0:
        positivos = positivos+ 1
    else:
        negativos = negativos + 1


print(f'Del rango {r1} al {r2} hay:\n'
      f'{positivos} numeros posivos\n'
      f'{negativos} numeros negativos')