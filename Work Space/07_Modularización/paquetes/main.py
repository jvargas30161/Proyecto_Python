import my_paquete.aritmetica as a


def main():
    suma = a.sumar(4, 5, 6, 7, 8, 9, 101500)
    resta = a.restar(1500, 50)
    potencia = a.potencia(3,30)

    print("La suma es: ", suma)
    print("La resta es: ", resta)
    print("La potencia es: ", potencia)

if __name__ == '__main__':
    main()
