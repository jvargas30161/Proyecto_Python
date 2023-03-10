# Módulo de números de Fibonacci

def fibo(n):
    a, b = 0, 1
    while  a < n:
        print(a, end=" ")
        a, b = b, a + b
        ### Que es lo que hace esta secuencia, iniciar de 1,1 para la siguiente secuencia suma de 1 + 1 = 2
        # luego la siguiente suma hace 2 + 1 = 3 etc

    print()

def fibo2(n):
    resultado = []
    a, b = 0, 1
    while  a < n:
        resultado.append(a)
        print(a, end=" ")
        a, b = b, a + b

    return resultado


