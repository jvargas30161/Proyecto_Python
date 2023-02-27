### Varias funciones integradas.

print("==========================número entero=========================")
## int ==>>> NUmero entero
print(int("15"))

print("==========================número floante========================")
## float ==>>> NUmero flotante
print(float("150"))

print("==========================dato string===========================")
## str ==>>> String
print(str("150"))

print("==================dato len cantidad de caracteres =============") #Cantidad de caracteres
## len ==>>> len cantidad de caracteres
print(len("Jorge Alexander Vargas Sanchez tiene 47 años"))
print(len("150"))

print("==========================dato round========================")
## round ==>>> Redondeo de números
print(round(4.8))  ### Redondeo de numero
print(round(4.85225936,2))  ### Redondeo de numero le pido que redondee a dos decimales


print("==========================dato eval========================")
## eval ==>>>
print(eval("150+50"))  ### a pesar de ser cadena de caracteres, va a enviar la solución.


print("==========================dato abs========================")
## abs Devuelve el valor absoluto de un número
print(abs(-150))
print(abs(150))

print("==========================dato bin========================")
## bin ==>>> dato binario
print(bin(100))
print(bin(120))

print("==========================dato bin a int========================")
## round ==>>> NUmero flotante
print(int(0b1100100))
print(int(0b1111000))

print("==========================dato a hex ========================")
## round ==>>> NUmero flotante
print(hex(150))
print(hex(12))

print("==========================dato de hex a int ========================")
## round ==>>> NUmero flotante
print(int(0x96))
print(int(0xc))

print("=================para ver la ayuda de python===================")
help()