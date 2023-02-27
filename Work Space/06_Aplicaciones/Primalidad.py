# ##Práctica 02: Primalidad
# 	Crear un sistema que detecte si un numero es primo o no
# 	Para solucionar este problema se requiere que el usuario ingres un numero por teclado y el
# sistema detecte si es primo o no.
# 	Un numero primo es aquel que se puede dividir solo dos veces por 1 y por sí misma.

def es_primo(numero):
    contador = 0

    for i in range(1, numero+1):
        if i == 1 or i == numero:
            continue

        if numero % i == 0:
            contador +=1

    if contador == 0:
        return True
    else:
        return False

def main():
    numero = int(input("Ingrese un Número: "))

    if es_primo(numero):
        print (f"El Número {numero} es primo")
    else:
        print(f"El numero {numero} no es primo")

if __name__ == '__main__':
    main()