## Expresiones Anidadas.
a = 3
b = 10
"""
* Multiplicación 
-Resta
** eleva 
>= Mayor o Igual (operador relacional)
Primiero resuelve lo de paréntesis
Luego resuelve expresiones aritméticas. primero la potencia (2 ** b)
Luego resuelve la multiplicación y luego la resta
Luego resuelve los operadores lógicos.
"""
print (a%b)
print (a * b - 2 ** b >=20 and not (a % b) !=0)
print (a * b - 2 ** b >=10 or not (a % b) !=0)
print (a * b - 2 ** b >=2 or (a % b) !=0)
print (a * b - 2 ** b >=5 or (a % b) !=0)
