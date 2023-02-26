"""Practica
01: Calcular cociente y el Residuo de dos números enteros
Enunciado: halar el cociente y el residuo (resto) de dos números enteros.
Análisis: para la solución de este problema, se requiere que el usuario ingrese dos números enteros y el sistema
realice el cálculo respectivo para hallar el cociente y residuo, para esto use la siguiente expresión.
"""

print ("calcular cociente  residuo")
a= input ("Ingrese el primer número: ")
b= input ("Ingrese el segundo número: ")

a= int(a)
b=int(b)

cociente = a // b
residuo =  a % b
print("El Cociente es: ", cociente)
print("El residuo es:", residuo)