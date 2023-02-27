#### calcularemos el factorial de un número
print("===================Primer Ejemplo ========================")
def factorial(n):
    print ("Valor Inicial =>", n)
    if n > 1:
        n = n * factorial(n-1)
    print ("Valor Final =>", n)
    return n

f= factorial(4)
print("Su factorial es", f)


#### calcularemos el factorial de un número
print("===================Segundo Ejemplo colocando un input ========================")

def factorial(n):
    # print ("Valor Inicial =>", n)
    if n > 1:
        n = n * factorial(n-1)
    # print ("Valor Final =>", n)
    return n

n = int(input("Ingrese un número: "))

f= factorial(n)
print("Su factorial es", f)


#### calcularemos el factorial de un número
print("===================Tercer Ejemplo colocando un input Mejorado ========================")

def factorial(n):
    # print ("Valor Inicial =>", n)
    if n > 1:
        n = n * factorial(n-1)
    # print ("Valor Final =>", n)
    return n

n = int(input("Ingrese un número: "))

f= factorial(n)
print(f"Su factorial de {n} es", f)

